from rolepermissions.roles import AbstractUserRole

class Administrador(AbstractUserRole):
    available_permissions = {
        'cadastrar_produtos': True,
        'liberar_desconto': True,
        'cadastrar_catador': True,
}
    
class Catador(AbstractUserRole):
    available_permissions = {
        'realizar_vendas': True,
    }