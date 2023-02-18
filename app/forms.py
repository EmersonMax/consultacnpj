from django import forms

ESTADOS = [('AC', 'Acre'), ('AL', 'Alagoas'), ('Ap', 'Amapá'),('AM', 'Amazonas'),('BA', 'Bahia'),('CE', 'Ceará'),('DF', 'Distrito Federal'),('ES', 'Espírito Santo'),('GO', 'Goiás'),('MA', 'Maranhão'),('MT', 'Mato Grosso'),('MS', 'Mato Grosso do Sul'),('MG', 'Minas gerais'),('PA', 'Pará'),('PB', 'Paraíba'),('PR', 'Paraná'),('PE', 'Pernanbuco'),('PI', 'Piauí'),('RJ', 'Rio de Janeiro'),('RN', 'Rio Grande do Norte'),('RS', 'Rio Grande do Sul'),('AM', 'Amazonas'),('RO', 'Rondônia'),('RR', 'Roraima'),('SC', 'Santa catarina'),('SP', 'São Paulo'),('SE', 'Sergipe'),('TO', 'Tocatins')]

class CnpjForm(forms.Form):
    cnpj = forms.CharField(max_length = 14)
    estado = forms.ChoiceField(widget=forms.Select, choices=ESTADOS)
    cnpj.widget.attrs["class"] = ""
    estado.widget.attrs["class"] = "state"