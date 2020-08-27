from django import forms
from .helper import k


class SignForm(forms.Form):

    department = forms.ChoiceField(label="Departamento*",
                                   required=True,
                                   widget=forms.Select({'id':'tag_department',
                                                     'class':'form-control'
                                                     }),
                                   choices=[(None,"Seleccione una opción")] +
                                   list(zip(k.keys(),k.keys()))
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

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["city"].choices=[(None,"-----------------------------")]

        if "department" in self.data:
            try:
            # rebuilding form definition to be able to pass validation when
            # using ajax with form
                choices = list(
                    zip(k[self.data["department"]],k[self.data["department"]])
                    )
                choices.extend([(False,"Seleccione ciudad")])

                self.fields["city"].choices = choices
            except (ValueError, TypeError):
                self.fields["city"]
