from django import forms


class SignForm(forms.Form):

    department = forms.ChoiceField(label="Departamento*",
                                   required=True,
                                   widget=forms.Select({'id':'tag_department',
                                                     'class':'form-control'
                                                     })
                                   )
    city = forms.ChoiceField(label="Ciudad*",
                             required=True,
                             widget=forms.Select({'id':'tag_city',
                                                'class':'form-control'
                                                })
                             )
    name = forms.CharField(label="Nombre*",
                            max_length=50,
                            required=True,
                            widget=forms.TextInput({'class':'form-control',
                                                    "placeholder":"Nombre",
                                                    'size':'37em'
                                                    })
                            )
    email = forms.EmailField(label="Email*",
                            max_length=30,
                            required=True,
                            widget=forms.EmailInput({'class':'form-control',
                                                    "placeholder":"Email",
                                                    'size':'37em',
                                                    })
                            )

