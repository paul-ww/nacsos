from django import forms
from django.forms.widgets import TextInput, Select, CheckboxInput, CheckboxSelectMultiple, HiddenInput, ClearableFileInput
from .models import *
from dal import autocomplete
from tmv_app.models import *
import cities


class ProjectForm(forms.ModelForm):
    class Meta:
        model = (Project)
        fields = ('title', 'description',)

class QueryEntryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['title', 'database', 'credentials', 'wos_collection', 'wos_editions', 'text']
        wos_specific = 'wos-specific'
        widgets = {
            'title': TextInput(),
            'database': Select(),
            'credentials': CheckboxInput(attrs={'class': wos_specific}),
            'wos_collection': Select(attrs={'class': wos_specific}),
            'wos_editions': CheckboxSelectMultiple(attrs={'class': f'{wos_specific} core-specific'})
        }
        help_texts = {
            'database': '"Internal" queries compare and combine two existing queries, \
                identified by their IDs, using the operators "NOT", "OR" and "AND"; \
                e.g. "36 AND 42", or "42 NOT 36".',
            'credentials': 'Tick to use the credentials saved on your \
                <a href="{% url "scoping:userpage" project.id %}">user page',
            'wos_collection': 'Choose the web of science database you would like to search. \
                Availability may depend on your credentials. The default option is the Web of \
                Science Core Collection). N.B. anything other than WoS Core may result in more \
                results but with less information about them.',
            'wos_editions': 'Narrow the search down to specific editions (availability \
                may depend on your credentials). If no option is picked, all editions \
                are included.'
        }

    def __init__(self, *args, **kwargs):
        is_staff = kwargs.pop('is_staff')
        super(QueryEntryForm, self).__init__(*args, **kwargs)
        if is_staff:
            self.fields['database'].initial = 'WoS'
            self.fields['wos_collection'].initial = 'core'
            self.fields['wos_editions'].initial = []
        if not is_staff:
            self.fields['database'].choices = [('intern','Internal')]
            for field_name in ['credentials', 'wos_collection', 'wos_editions']:
                self.fields[field_name].widget = HiddenInput()

class QueryUploadForm(forms.ModelForm):
    class Meta:
        model = Query
        fields=["query_file"]
        widgets = {
            'query_file': ClearableFileInput(attrs={'multiple': True})
        }
        help_texts = {
            'query_file': 'Upload a Web of Science or Scopus or RIS file you have \
                downloaded yourself. Accepted formats are WoS/Scopus text files or \
                RIS files',
        }

class CatIntForm(forms.Form):
    def __init__(self,*args,**kwargs):
        doc_id = kwargs.pop('doc_id',None)
        cat_id = kwargs.pop('cat_id', None)
        user_id = kwargs.pop('user_id', None)
        super(CatIntForm, self).__init__(*args, **kwargs)
        self.fields['doc_id'].initial = doc_id
        self.fields['cat_id'].initial = cat_id
        self.fields['user_id'].initial = user_id
        try:
            duc = DocUserCat.objects.get(doc__id=doc_id,category__id=cat_id,user__id=user_id)
            self.fields['number'].initial = duc.number
        except:
            pass

    doc_id = forms.IntegerField(widget=forms.HiddenInput())
    cat_id = forms.IntegerField(widget=forms.HiddenInput())
    user_id = forms.IntegerField(widget=forms.HiddenInput())
    number = forms.IntegerField(label="Number")

class CatYearForm(forms.Form):
    def __init__(self,*args,**kwargs):
        doc_id = kwargs.pop('doc_id',None)
        cat_id = kwargs.pop('cat_id', None)
        user_id = kwargs.pop('user_id', None)
        super(CatYearForm, self).__init__(*args, **kwargs)
        self.fields['doc_id'].initial = doc_id
        self.fields['cat_id'].initial = cat_id
        self.fields['user_id'].initial = user_id
        try:
            duc = DocUserCat.objects.get(doc__id=doc_id,category__id=cat_id,user__id=user_id)
            self.fields['baseline_year_2'].initial = duc.baseline_year_2
            self.fields['observation_year_2'].initial = duc.observation_year_2
            self.fields['baseline_year_1'].initial = duc.baseline_year_1
            self.fields['observation_year_1'].initial = duc.observation_year_1
            self.fields['duration'].initial = duc.duration
        except:
            pass

    doc_id = forms.IntegerField(widget=forms.HiddenInput())
    cat_id = forms.IntegerField(widget=forms.HiddenInput())
    user_id = forms.IntegerField(widget=forms.HiddenInput())
    baseline_year_1 = forms.IntegerField(label="Observation period 1 - start")
    baseline_year_2 = forms.IntegerField(label="Observation period 1 - end")
    observation_year_1 = forms.IntegerField(label="Observation period 2 - start")
    observation_year_2 = forms.IntegerField(label="Observation period 2 - end")
    duration = forms.FloatField(label="Duration (years - enter decimal for periods less than 1 year)")

class TextPlaceForm(forms.Form):
    def __init__(self,*args,**kwargs):
        doc_id = kwargs.pop('doc_id',None)
        cat_id = kwargs.pop('cat_id', None)
        user_id = kwargs.pop('user_id', None)
        super(TextPlaceForm, self).__init__(*args, **kwargs)
        self.fields['doc_id'].initial = doc_id
        self.fields['cat_id'].initial = cat_id
        self.fields['user_id'].initial = user_id
        try:
            duc = DocUserCat.objects.get(doc__id=doc_id,category__id=cat_id,user__id=user_id)
            self.fields['places'].initial = list(duc.places.all().values_list('id',flat=True))
        except:
            pass

    doc_id = forms.IntegerField(widget=forms.HiddenInput())
    cat_id = forms.IntegerField(widget=forms.HiddenInput())
    user_id = forms.IntegerField(widget=forms.HiddenInput())
    places = forms.ModelChoiceField(
        queryset=TextPlace.objects.filter(name__icontains="foo"),
        widget=autocomplete.ModelSelect2Multiple(
            url="scoping:textplace-autocomplete",
            attrs={
                'data-minimum-input-length': 2
            }
        )
    )

class TextFreeForm(forms.Form):
    def __init__(self,*args,**kwargs):
        doc_id = kwargs.pop('doc_id',None)
        cat_id = kwargs.pop('cat_id', None)
        user_id = kwargs.pop('user_id', None)
        super(TextFreeForm, self).__init__(*args, **kwargs)
        self.fields['doc_id'].initial = doc_id
        self.fields['cat_id'].initial = cat_id
        print(cat_id)
        self.fields['user_id'].initial = user_id
        try:
            duc = DocUserCat.objects.get(doc__id=doc_id,category__id=cat_id,user__id=user_id)
            self.fields['texts'].initial = list(duc.texts.all().values_list('id',flat=True))
        except:
            pass


    doc_id = forms.IntegerField(widget=forms.HiddenInput())
    cat_id = forms.IntegerField(widget=forms.HiddenInput())
    user_id = forms.IntegerField(widget=forms.HiddenInput())
    texts = forms.ModelChoiceField(
        queryset=TextFree.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url="scoping:textfree-autocomplete",
            attrs={
                'data-minimum-input-length': 2
            },
            forward = ['cat_id'],
        )
    )

class CountryForm(forms.Form):
    def __init__(self,*args,**kwargs):
        doc_id = kwargs.pop('doc_id',None)
        cat_id = kwargs.pop('cat_id', None)
        user_id = kwargs.pop('user_id', None)
        super(CountryForm, self).__init__(*args, **kwargs)
        self.fields['doc_id'].initial = doc_id
        self.fields['cat_id'].initial = cat_id
        self.fields['user_id'].initial = user_id
        try:
            duc = DocUserCat.objects.get(doc__id=doc_id,category__id=cat_id,user__id=user_id)
            self.fields['places'].initial = list(duc.countries.all().values_list('id',flat=True))
        except:
            pass

    doc_id = forms.IntegerField(widget=forms.HiddenInput())
    cat_id = forms.IntegerField(widget=forms.HiddenInput())
    user_id = forms.IntegerField(widget=forms.HiddenInput())
    places = forms.ModelChoiceField(
        queryset=cities.models.Country.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url="scoping:country-autocomplete",
            attrs={
                'data-minimum-input-length': 2
            }
        )
    )
    #class Meta

class RiskOfBiasForm(forms.ModelForm):

    class Meta:
        model = (RiskOfBias)
        exclude = ()


class TwitterForm(forms.Form):
    def __init__(self,*args,**kwargs):
        p = kwargs.pop('p',Project.objects.all())
        super(TwitterForm, self).__init__(*args, **kwargs)
        self.fields['users'].queryset = User.objects.filter(
            projectroles__project=p
        )
        if hasattr(p, 'pk'):
            self.fields['pid'].initial = p.pk
    sample_size = forms.IntegerField(min_value=0, max_value=1000)
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    double_check = forms.BooleanField(
        help_text="Click to make sure each tweet is seen by all users,"
        +" if not each tweet will be seen by a single user"
        )
    pid = forms.IntegerField(widget=forms.HiddenInput())

class MetaAssignmentForm(forms.Form):
    def __init__(self,*args,**kwargs):
        p = kwargs.pop('p',Project.objects.all())
        super(MetaAssignmentForm, self).__init__(*args, **kwargs)
        self.fields['users'].queryset = User.objects.filter(
            projectroles__project=p
        )
        self.fields['pid'].initial = p.pk
    users = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    split = forms.BooleanField(help_text="check to split documents between all users, leave blank to assing all documents to all users")
    sample = forms.DecimalField(
        max_value=1,min_value=0.01,decimal_places=2,
        help_text="The (random) fraction of documents to be assigned - set as 1 to assign all documents."
    )
    ac = forms.CharField(widget=forms.HiddenInput())
    key = forms.CharField(widget=forms.HiddenInput())
    pid = forms.IntegerField(widget=forms.HiddenInput())

class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('qs',Category.objects.all())
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields["parent_category"] = forms.ModelChoiceField(
                required=False,
                queryset=qs
            )
    level = forms.IntegerField(
        min_value=1, max_value=9
    )
    parent_category = forms.ModelChoiceField(
        required=False,
        queryset=Category.objects.all()
    )
    class Meta:
        model = (Category)
        fields = ('name','level','description','parent_category')
        widgets = {
          'name': forms.TextInput(attrs={'class': "form-control"}),
          'description': forms.TextInput(attrs={'class': "form-control"}),
        }

class InterventionForm(forms.ModelForm):
    name = forms.CharField()
    class Meta:
        model = InterventionType
        exclude = ('project',)

class ControlsForm(forms.Form):
    name = forms.CharField()
    controls = forms.CharField(widget=forms.HiddenInput(),required=False)

class ExclusionForm(forms.Form):
    name = forms.CharField()
    exclusion = forms.CharField(widget=forms.HiddenInput(),required=False)

class PopCharForm(forms.ModelForm):
    name = forms.CharField()
    unit = forms.CharField(required=False)
    class Meta:
        model = PopCharField
        exclude = ('project',)

class InterventionSubtypeForm(forms.ModelForm):
    name = forms.CharField()
    class Meta:
        model = InterventionSubType
        exclude = ('project',)

class NewDoc(forms.ModelForm):

    url = forms.URLField(
        required=False,
        help_text="""
            If you have a link to the online version of this document,
            please provide it here so we can check whether it's been added already
        """
    )

    class Meta:
        model = (Doc)
        fields = ('dtype','url',)

class DocForm2(forms.ModelForm):

    py = forms.IntegerField(
        #initial=2017,
        label="Year Published",
        help_text="Leave as 0 if unpublished"
    )
    so = forms.CharField(
        label="Source Title",
        help_text="Enter the journal or book title",
        max_length=250,
        required=False
    )
    doc = forms.IntegerField()
    class Meta:
        model = (WoSArticle)
        fields = ('doc','ti','ab','py','so',)

    def __init__(self,*args,**kwargs):
        so = kwargs.pop('so',False)
        super(DocForm2, self).__init__(*args, **kwargs)
        self.fields['doc'].widget = forms.HiddenInput()
        if so:
            self.fields['so'].required = True


class AuthorForm(forms.ModelForm):

    surname = forms.CharField(max_length=50)
    initials = forms.CharField(max_length=10)
    class Meta:
        model = (DocAuthInst)
        fields = ('position','surname','initials',)

    def __init__(self,*args,**kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.fields['position'].widget = forms.HiddenInput()


class UploadDocFile(forms.ModelForm):
    doc = forms.IntegerField()
    class Meta:
        model = (DocFile)
        fields = ('doc','file',)
    def __init__(self,*args,**kwargs):
        super(UploadDocFile, self).__init__(*args, **kwargs)
        self.fields['doc'].widget = forms.HiddenInput()

class FieldChoiceForm(forms.Form):
    project = forms.IntegerField()
    field = forms.CharField()
    name = forms.CharField()
    def __init__(self,*args,**kwargs):
        super(FieldChoiceForm, self).__init__(*args, **kwargs)
        self.fields['project'].widget = forms.HiddenInput()
        self.fields['field'].widget = forms.HiddenInput()

class DeleteDocField(forms.Form):
    delete = forms.IntegerField()
    def __init__(self,*args,**kwargs):
        super(DeleteDocField, self).__init__(*args, **kwargs)
        self.fields['delete'].widget = forms.HiddenInput()

class ValidatePasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='You need to enter your password to do this. It cannot be undone',
    )
    widgets = {
        'password': forms.PasswordInput()
    }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(ValidatePasswordForm, self).__init__(*args,**kwargs)

    def clean_password(self):
        password = self.cleaned_data['password']
        if not self.user.check_password(password):
            raise forms.ValidationError('Invalid password')
        return password

class ProjectRoleForm(forms.ModelForm):
    class Meta:
        model = (ProjectRoles)
        fields = ('user', 'role',)

class UpdateProjectRoleForm(forms.ModelForm):
    user = forms.CharField(disabled=True)
    class Meta:
        model = (ProjectRoles)
        fields = ('user', 'role',)
        #widgets = {'user': forms.HiddenInput()}

class TagForm(forms.ModelForm):
    title = forms.CharField(label='Tag title', max_length=100)
    class Meta:
        model = (Tag)
        fields = ('title',)


class TopicModelForm(forms.ModelForm):
    METHOD_CHOICES = (
        ('NM','nmf'),
        ('LD', 'lda'),

    )
    method = forms.ChoiceField(widget=forms.Select,choices=METHOD_CHOICES)
    class Meta:
        model = (RunStats)
        fields = (
            'min_freq','max_df','max_features','limit',
            'ngram','fulltext','citations',
            'fancy_tokenization',
            'K','alpha','beta','max_iter','db',
            'method', 'lda_learning_method','lda_library'
        )
        exclude = (
            'topic',
            'dynamictopic',
            'term',
            'run_id',
            'query',
            'process_id',
            'start',
            'batch_count',
            'last_update',
            'topic_titles_current',
            'empty_topics',
            'topic_scores_current',
            'topic_year_scores_current',
            'nmf_time',
            'tfidf_time',
            'db_time',
            'status',
            'parent_run_id',
            'docs_seen',
            'notes',
            'psearch',
            #'method',
            'error',
            'errortype',
            'iterations',
            'max_topics',
            'term_count',
            'dthreshold',
            'dyn_win_threshold',
            'periods',
            'coherence',
        )
        #fields = ('K','alpha','limit','ngram','min_freq','max_df','max_features','max_iter')
