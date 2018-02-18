# mitigate heap fragmentation issues by pre-loading major libraries
import gc
gc.collect()
import agnostic
gc.collect()
import unittest
gc.collect()

def yes_no(q, default=True):
    a = input(q + " (Y/n)?" if default else " (y/N)?")
    a=a.lower()
    if a == '':
        return default
    elif a == "n":
        a = False
    elif a == "y":
        a = True
    return a

def multi_choice(q, choices, defaultPos=None):
    if defaultPos is not None:
        print("{} [{}]?".format(q, defaultPos))
    else:
        print(q + "?")
    for pos, choice in enumerate(choices):
        print("{}) {}".format(pos, choice))
    a = input()
    a=a.lower()
    try:
        if a == '':
            a = defaultPos
        else:
            a = int(a)
        return choices[a]
    except Exception as e:
        print(e)
        return None


def test_module(module, runner=None):
    import unittest
    if runner is None:
        runner = unittest.TestRunner()
    suite = unittest.TestSuite()
    for key in dir(module):
        val = getattr(module, key)
        try:
            if issubclass(val, unittest.TestCase):
                suite.addTest(val)
        except:
            pass
    return runner.run(suite)

def test_module_name(absolute, runner=None):
    print("Testing {}".format(absolute))
    module=__import__(absolute)
    relatives = absolute.split(".")
    if len(relatives) > 1:
        for relative in relatives[1:]:
            module = getattr(module, relative)
    return test_module(module, runner)

def test_interactive(*module_names):
    for module_name in module_names:
        if yes_no("Test {}".format(module_name)):
            gc.collect()
            test_module_name(module_name)


def test_prepare(casetype):
    case = casetype()
    case.setUp()


def main():
    test_interactive(
        "testing.implementation.all.digitalio",
    )