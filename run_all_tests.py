#!/usr/bin/env python3
"""
Run all test cases for the Traveling Ethiopia Search Problem project
"""

import sys
import os

def run_tests():
    """Run all question tests"""
    print("=" * 70)
    print("Traveling Ethiopia Search Problem - All Tests")
    print("=" * 70)
    print()
    
    # Question 1
    try:
        print("\n" + "=" * 70)
        from question1.test_question1 import test_question1
        test_question1()
    except Exception as e:
        print(f"Error in Question 1: {e}")
        import traceback
        traceback.print_exc()
    
    # Question 2
    try:
        print("\n" + "=" * 70)
        from question2.test_question2 import test_question2
        test_question2()
    except Exception as e:
        print(f"Error in Question 2: {e}")
        import traceback
        traceback.print_exc()
    
    # Question 3
    try:
        print("\n" + "=" * 70)
        from question3.test_question3 import test_question3
        test_question3()
    except Exception as e:
        print(f"Error in Question 3: {e}")
        import traceback
        traceback.print_exc()
    
    # Question 4
    try:
        print("\n" + "=" * 70)
        from question4.test_question4 import test_question4
        test_question4()
    except Exception as e:
        print(f"Error in Question 4: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 70)
    print("All tests completed!")
    print("=" * 70)


if __name__ == "__main__":
    run_tests()

