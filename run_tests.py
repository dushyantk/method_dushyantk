import cmd
import sys

class run_tests(cmd.Cmd):
    
    prompt = "INPUT [flatten OR tempo]/>"

    def do_flatten(self, arg):
        
        if sys.version_info.major == 3:
            from tests.flatten_list3 import flatten3 as flatten
        else:
            from tests.flatten_list import flatten2 as flatten

        input_list1 = [[[1, 2, 3], [4, 5]], 6]
        input_list2 = [[1, 2,[3]],4]
        print(input_list1, '-->', list(flatten(input_list1)))
        print(input_list2, '-->', list(flatten(input_list2)))

    def do_tempo(self, arg):
        from tests.how_cold import TestTempTracker
        import unittest as ut
        print("Running TEMPERATURE test.")
        test_cases = ut.TestLoader().loadTestsFromTestCase(TestTempTracker)
        ut.TextTestRunner(verbosity=2).run(test_cases)

run_tests().cmdloop()
