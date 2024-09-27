import typing


class Sotrudnik:
    def __init__(self, email: str, fname: str, name: str, sname: str, login: str, password: str) -> None:
        """
        :param email: почта сотрудника
        :param fname: фамилия сотрудника
        :param name: имя сотрудника
        :param sname: отчество сотрудника
        :param login: логин сотрудника
        :param password: пароль сотрудника
        """
        self.email = email
        self.fname = fname
        self.name = name
        self.sname = sname
        self.login = login
        self.password = password
