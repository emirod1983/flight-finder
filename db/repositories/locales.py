from db.repositories.base import BaseRepository

class LocalesRepository(BaseRepository):
    def _get_table(self):
        return self.schema.tables['locales']