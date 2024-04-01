import re
from cookiecutter.utils import simple_filter


@simple_filter
def regex_format(input_str, pattern):
    match = re.search(pattern, input_str)
    if match:
        return match.group(0)
    else:
        return input_str

