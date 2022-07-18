from typing import List


# finix list implementation
class FinixList:
    def __init__(self, some_list, method, **kwargs):
        self._method = method
        self._kwargs = kwargs

        if hasattr(some_list, 'embedded'):
            tmp = some_list.embedded
            if isinstance(tmp, dict):
                for key in tmp:
                    self._contents = tmp[key]
                    break
            else:
                self._contents = []
        else:
            self._contents = []
        
        self.content = []
        if self._contents != []:
            for item in self._contents:
                finix_item = FinixObject(item)
                self.content.append(finix_item)

        if hasattr(some_list, 'links'):
            self.links = some_list.links
        else:
            self.links = 'no_links_received'

        if hasattr(some_list, 'page'):
            self.page = some_list.page
        else:
            self.page = 'no_page_received'
    
        self.has_more = False
        self._next_case = 0
        if 'next_cursor' in self.page and self.content != []:
            if self.page['next_cursor'] != 'Null' and self.page['next_cursor'] != 'null':
                self.has_more = True
                self._next_case = 1
        
        if 'offset' in self.page and self.content != []:
            if self.page['offset'] + self.page['limit'] <= self.page['count']:
                self.has_more = True
                self._next_case = 2
                     
    def __len__(self):
        return len(self.content)
    
    def __getitem__(self,index):
        return self.content[index]

    def __iter__(self):
        return iter(self.content)
    
    def list_next(self):
        if not self.has_more:
            raise PaginationException()

        else:
            if self._next_case == 1:
                para = self._kwargs
                para['after_cursor'] = self.page['next_cursor']
                return self._method(**para)
            
            if self._next_case == 2:
                para = self._kwargs
                para['offset'] = self.page['offset'] + self.page['limit']
                return self._method(**para)


# custom exception raised when list_next() fails
class PaginationException(Exception):
    def __init__(self):
        self.message = 'list_next() fails: either pagination information is missing or there is no more resource to fetch!'
    
    def __str__(self):
        return self.message


# finix object implementation
class FinixObject:
    def __init__(self,some_dict):
        self.__dict__.update(some_dict)

    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} : {}'.format(item, self.__dict__[item]) for item in self.__dict__))


# finix error implementation
class FinixError:
    def __init__(self, some_dict):
        self.__dict__.update(some_dict)

        if 'authorization' in some_dict:
            self.authorization = some_dict['authorization']
        else:
            self.authorization = None
        
        if 'code' in some_dict:
            self.code = some_dict['code']
        else:
            self.code = None

        if 'failure_code' in some_dict:
            self.failure_code = some_dict['failure_code']
        else:
            self.failure_code = None

        if 'failure_message' in some_dict:
            self.failure_message = some_dict['failure_message']
        else:
            self.failure_message = None

        if 'logref' in some_dict:
            self.logref = some_dict['logref']
        else:
            self.logref = None

        if 'message' in some_dict:
            self.message = some_dict['message']
        else:
            self.message = None

        if 'transfer' in some_dict:
            self.transfer = some_dict['transfer']
        else:
            self.transfer = None

        if 'field' in some_dict:
            self.field = some_dict['field']
        else:
            self.field = None

    def __str__(self):
        return  str(self.__class__) + '\n'+ '\n'.join(('{} : {}'.format(item, self.__dict__[item]) for item in self.__dict__))

# error list implementation
class ErrorList:
    errors: List[FinixError]

    def __init__(self, some_dict=None):
        self.errors = []
        if isinstance(some_dict, dict):
            if '_embedded' in some_dict:
                if 'errors' in some_dict['_embedded']:
                    if isinstance(some_dict['_embedded']['errors'], list):
                        for item in some_dict['_embedded']['errors']:
                            self.errors.append(FinixError(item))
        if self.errors == []:
            self.no_error_body = True
        else:
            self.no_error_body = False
                     
    def __len__(self):
        return len(self.errors)
    
    def __getitem__(self,index):
        return self.errors[index]

    def __iter__(self):
        return iter(self.errors)
    