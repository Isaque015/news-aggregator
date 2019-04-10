from sqlalchemy import UniqueConstraint
from sqlalchemy_filters import apply_filters

from app.settings.database_settings import session


class BaseModel():

    def __is_not_empty__(self, field):
        return bool(field and field.strip())

    def __get_attr_nullable_false__(self):
        attrs_with_not_null = []

        for attr in iter(self.__table__.columns):
            if not attr.nullable and attr.name != 'id':
                attrs_with_not_null.append(attr.name)
        return attrs_with_not_null

    def __do_not_let_save_empty__(self):
        attrs_nullable_false = self.__get_attr_nullable_false__()

        for attr in attrs_nullable_false:
            attr_instance = getattr(self, attr)
            if not self.__is_not_empty__(attr_instance):

                return {
                    'status': False,
                    'msg': f'{attr} not allow blank'
                }
        return {'status': True}

    def __get_attr_with_unique__(self):
        attrs_with_unique_true = []

        for constraint in iter(list(self.__table__.constraints)):
            if isinstance(constraint, UniqueConstraint):
                attrs_column = dir(constraint.columns)
                attr = [
                    attr for attr in attrs_column if not attr.startswith('__')
                ]

                attrs_with_unique_true.append(attr[0])

        return attrs_with_unique_true

    def __verify_attr_exists__(self):
        attrs = self.__get_attr_with_unique__()
        query = session.query(self.__class__)

        for attr in attrs:
            value_attr_self = getattr(self, attr)

            filter_spec = [
                {'field': attr, 'op': '==', 'value': value_attr_self}
            ]

            filtered_query = apply_filters(query, filter_spec)
            result = filtered_query.all()

            if result:
                response = {
                    'status': False,
                    'msg': f'the {value_attr_self} already exists in {attr}'
                }
                return response
        return {'status': True}
