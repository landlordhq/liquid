"""Golden tests cases for testing liquid's `cycle` tag."""

from liquid.golden.case import Case

cases = [
    Case(
        description="no identifier",
        template=(
            r"{% cycle 'some', 'other' %}"
            r"{% cycle 'some', 'other' %}"
            r"{% cycle 'some', 'other' %}"
        ),
        expect="someothersome",
    ),
    Case(
        description="with identifier",
        template=(
            r"{% cycle 'foo': 'some', 'other' %}"
            r"{% cycle 'some', 'other' %}"
            r"{% cycle 'foo': 'some', 'other' %}"
        ),
        expect="somesomeother",
    ),
    Case(
        description="different items",
        template=(
            r"{% cycle '1', '2', '3' %}"
            r"{% cycle '1', '2' %}"
            r"{% cycle '1', '2', '3' %}"
        ),
        expect="112",
    ),
    Case(
        description="integers",
        template=r"{% cycle 1, 2, 3 %}{% cycle 1, 2, 3 %}{% cycle 1, 2, 3 %}",
        expect="123",
    ),
    # Case(
    #     description="some global variables",
    #     template=r"{% cycle a, b, c %}{% cycle a, b, c %}{% cycle a, b, c %}",
    #     expect="123",
    #     globals={"a": 1, "b": 2, "c": 3},
    # ),
    Case(
        description="variable name",
        template=r"{% cycle a: 1, 2, 3 %}{% cycle a: 1, 2, 3 %}{% cycle a: 1, 2, 3 %}",
        expect="123",
        globals={"a": "foo"},
    ),
    Case(
        description="changing variable name",
        template=(
            r"{% cycle a: 1, 2, 3 %}"
            r"{% assign a = 'bar' %}"
            r"{% cycle a: 1, 2, 3 %}"
            r"{% cycle a: 1, 2, 3 %}"
        ),
        expect="112",
        globals={"a": "foo"},
    ),
    # Case(
    #     description="named with different items",
    #     template=(
    #         r"{% cycle 'a': 1, 2, 3 %}"
    #         r"{% cycle 'a': 7, 8, 9 %}"
    #         r"{% cycle 'a': 1, 2, 3 %}"
    #     ),
    #     expect="183",
    # ),
]
