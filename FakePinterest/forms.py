from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length,ValidationError
from FakePinterest.models import Usuario


class FormLogin(FlaskForm):
    email = StringField("E-mail", validators =[DataRequired(), Email()] )
    senha = PasswordField("Senha", validators = [DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")



class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators = [DataRequired(), Email()])
    username = StringField("nome de usuario", validators = [DataRequired()])
    senha = PasswordField("senha", validators = [DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField("confirmação de Senha", validators =[DataRequired(), EqualTo('senha')])
    botao_confirmacao = SubmitField ("Criar conta")

    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            return ValidationError("Email já cadastrado")


class FormFoto(FlaskForm):
    foto = FileField("foto", validators=[DataRequired()])
    botao_confirmacao = SubmitField("enviar")