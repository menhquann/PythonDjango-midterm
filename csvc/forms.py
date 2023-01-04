from django import forms
from .models import Csvc, Department

class CsvcForm(forms.ModelForm):
    code = forms.CharField(
        label='Ma Phong',
        widget=forms.TextInput(
            attrs = {'class':'form-control',
             'placeholder' : 'Ma Phong'}
        )
    )
    name = forms.CharField(
        required=False,
        label='Ten Phong',
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder' : 'Ten Phong'
            }
        )
    )
    den = forms.IntegerField(
        label='Den',
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder' : 'So luong'
            }
        )
    )
    ban_ghe = forms.IntegerField(
        label='Ban Ghe',
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder' : 'So luong'
            }
        )
    )
    may_chieu = forms.IntegerField(
        label='May Chieu',
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder' : 'So luong'
            }
        )
    )
    quat = forms.IntegerField(
        label='Quat',
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder' : 'So luong'
            }
        )
    )
    dieu_hoa = forms.IntegerField(
        label='Dieu Hoa',
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder' : 'So luong'
            }
        )
    )

    
    class Meta:
        model = Csvc
        fields = ['name', 'code', 'den','ban_ghe','may_chieu','quat','dieu_hoa','department']
    
    # def __init__(self, *args, **kwargs):
    #     super(StudentForm,self).__init__(*args,**kwargs)
    #     departmentObjs = Department.objects.all()
    #     departments = [(i.id, i.name) for i in departmentObjs]
    #     self.fields['department'].choices=departments
 
    # def clean_code(self, *args, **kwargs):
    #     new_code = self.cleaned_data.get('code')
    #     if not new_code.isnumeric():
    #         raise forms.ValidationError("The code shoulld be digit only!")
    #     return new_code
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith("dut.udn.vn"):
    #         raise forms.ValidationError("The email should end with dut.udn.vn!")
    #     return email

