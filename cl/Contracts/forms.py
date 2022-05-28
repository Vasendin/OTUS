from django.forms import ModelForm

from Contracts.models import Contract, Organization


class ContractCreateForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name)
            # print(field)
            field.widget.attrs['class'] = 'model-form'


class OrganizationCreateForm(ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name)
            # print(field)
            field.widget.attrs['class'] = 'model-form'