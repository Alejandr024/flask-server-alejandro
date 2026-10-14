from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    # Campo de texto obligatorio con validación de formato Email
    email = StringField("Correo Electrónico", validators=[DataRequired(), Email()])

    # Campo de contraseña obligatorio con longitud mínima
    password = PasswordField(
        "Contraseña",
        validators=[DataRequired(), Length(min=6, message="Mínimo 6 caracteres")],
    )

    submit = SubmitField("Iniciar Sesión")
