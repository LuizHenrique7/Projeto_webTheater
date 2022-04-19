class Categoria():

    def __init__(self, id: int, nome_categoria: str, nome_filme: str, image_path:str, descricao:str, video_path:str):
        self.__id = id
        self.__nome_categoria = nome_categoria
        self.__nome_filme = nome_filme
        self.__image_path = image_path
        self.__descricao = descricao
        self.__video_path = video_path


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome_categoria(self):
        return self.__nome_categoria

    @nome_categoria.setter
    def nome_categoria(self, value):
        self.__nome_categoria = value

    @property
    def nome_filme(self):
        return self.__nome_filme

    @nome_filme.setter
    def nome_filme(self, value):
        self.__nome_filme = value


    @property
    def image_path(self):
        return self.__image_path


    @image_path.setter
    def image_path(self, value):
        self.__image_path = value

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, value):
        self.__descricao = value

    @property
    def video_path(self):
        return self.__video_path

    @video_path.setter
    def video_path(self, value):
        self.__video_path = value



