class CodeNavigator:

    def where_is(self, knowledge, symbol):

        classes = knowledge["symbol_index"]["classes"]

        return classes.get(symbol)