def myfunc(self,            # gotta have self
           param1="value",  # values are cool
           param2=True,     # or False, whatever
           **kwargs):       # you never know
    pass



def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
myfunc        : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
self          : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.pyhton
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.python
 gotta have self : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
param1        : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.pyhton
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
"             : meta.function.parameters.python, meta.function.python, source.python, string.quoted.double.python
value         : meta.function.parameters.python, meta.function.python, source.python, string.quoted.double.python
"             : meta.function.parameters.python, meta.function.python, source.python, string.quoted.double.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.python
 values are cool : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
param2        : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.pyhton
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.python
True          : constant.language.python, meta.function.parameters.python, meta.function.python, source.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.python
 or False, whatever : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.python
              : meta.function.parameters.python, meta.function.python, source.python
*             : meta.function.parameters.python, meta.function.python, source.python
*             : meta.function.parameters.python, meta.function.python, source.python
kwargs        : meta.function.parameters.python, meta.function.python, source.python, variable.parameter.function.language.pyhton
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python
 you never know : comment.line.number-sign.python, source.python
              : source.python
pass          : keyword.control.flow.python, source.python