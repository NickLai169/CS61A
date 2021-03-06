test = {
  'name': 'or-macro',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (or-macro #t #f)
          #t
          scm> (or-macro #f #t)
          #t
          scm> (or-macro 0 #f)
          0
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (or-macro (/ 1 0) #t)
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (or-macro #t (/ 1 0))
          #t
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (or-macro #f (/ 1 0))
          SchemeError
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (or-macro (print 'hi) (print 'bye))
          hi
          scm> (or-macro (begin (print 'hi) #f) (print 'bye))
          hi
          bye
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': False,
      'setup': r"""
      scm> (load 'lab11)
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
