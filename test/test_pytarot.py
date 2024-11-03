import pytest

from src.pytarot import get_answers_of_wisdom, get_lucky_day, get_true_lover, get_positive_action

class Tests:
    #
    # Fixtures - these are functions that can do any optional setup or teardown before or after a test function is run.
    #

    @pytest.fixture
    def example_fixture(self):
        """
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        """

        # place any setup you want to do before any test function that uses this fixture is run

        yield  # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed

    #
    # Test functions
    #

    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"





    #true lover tests
    #test1
    def test_get_true_lover_non_empty(self):
        """
        Verify get_true_lover() function and make sure it returns a non-empty string.
        """
        result =  get_true_lover()
        
        # Check that the result is a non-empty string
        assert isinstance(result, str), "The result should be a string."
        assert len(result) > 0, "The result should not be an empty string."
    #test2
    def test_get_true_lover_content(self):
        """
        Verify get_true_lover() function and make sure it contains all the necessary elements.
        """
        result = get_true_lover()
        
        # Check for content
        jobs = ["Teacher", "Engineer", "Doctor", "Nurse", "Architect", "Software Developer", "Graphic Designer", "Chef", "Pilot", 
                "Lawyer", "Accountant", "Scientist", "Electrician", "Carpenter", "Mechanic", "Writer", "Artist", "Photographer", 
                "Pharmacist", "Veterinarian", "Social Worker", "Police Officer", "Firefighter", "Librarian", "Journalist", 
                "Marketing Specialist", "Salesperson", "Plumber", "Psychologist", "Data Analyst", "Financial Advisor", "Dentist", 
                "Actor", "Musician", "Farmer", "Translator", "Consultant", "Project Manager", "Researcher", "Event Planner", 
                "Web Developer", "Therapist", "Fitness Trainer", "Fashion Designer", "Interior Designer", "Animator", "Biologist", 
                "Chemist", "Historian"]
        
        heights = ["Very Short", "Short", "Below Average", "Average", "Above Average", "Tall", "Very Tall", "Extremely Tall"]
        eye_colors = ["Brown", "Blue", "Green", "Hazel", "Amber", "Gray", "Violet", "Black", "Red"]
        hair_colors = ["Black", "Brown", "Blonde", "Red", "Auburn", "Chestnut", "Gray", "White", "Silver", "Platinum Blonde", 
                    "Strawberry Blonde", "Blue", "Green", "Pink", "Purple", "Teal"]
        residences = ["House", "Apartment", "Condo", "Villa", "Cabin", "Cottage", "Mansion", "Farmhouse", "Bungalow", "Duplex", 
                    "Studio", "Loft", "Townhouse", "Mobile Home", "Penthouse", "Dormitory", "Hostel", "Boarding House", 
                    "Tiny House", "Yurt", "Chalet", "Tent", "RV", "Boat", "Caravan", "Castle", "Ranch", "Hut", "Treehouse", 
                    "Igloo", "Palace"]

        # Ensure that the output has all the elements
        assert any(job in result for job in jobs), "The result should contain a job title."
        assert any(height in result for height in heights), "The result should contain a height descriptor."
        assert any(eye_color in result for eye_color in eye_colors), "The result should contain an eye color."
        assert any(hair_color in result for hair_color in hair_colors), "The result should contain a hair color."
        assert any(residence in result for residence in residences), "The result should contain a residence type."
    #test3
    def test_get_true_lover_uniqueness(self):
        """
        Verify get_true_lover() function and make sure it has some uniqueness to its output.
        """
        results = {get_true_lover() for _ in range(10)}
        assert len(results) > 1, "The function should generate some unique profiles."
    #test4
    def test_get_true_lover_format_keywords(self):
        """
        Verify get_true_lover() function and make sure it has the mandatory keywords in the output.
        """
        result = get_true_lover()
        expected_keywords = ["who is", "with", "eyes", "hair", "lives in"]
        for keyword in expected_keywords:
            assert keyword in result, f"The result should contain '{keyword}'"


    #lucky day tests
    # Test 1: Ensure the function returns a valid string
    def test_get_lucky_day_non_empty(self):
        """
        Verify that get_lucky_day() returns a non-empty string.
        """
        result = get_lucky_day()
        
        # Check that the result is a non-empty string
        assert isinstance(result, str), "The result should be a string."
        assert len(result) > 0, "The result should not be an empty string."

    # Test 2: Ensure the output is in the correct format
    def test_get_lucky_day_format(self):
        """
        Verify that get_lucky_day() returns a result in the correct format (Month/Day).
        """
        result = get_lucky_day()
        
        try:
            month, day = result.split(' ')[-1].split('/')
            assert month.isalpha(), "The month should be in word format."
            assert day.isdigit() and 1 <= int(day) <= 31, "The day should be a number between 1 and 31."
        except ValueError:
            assert False, "The output format should be 'Your lucky day is: Month/Day'."

    # Test 3: Ensure the function covers all months
    def test_get_lucky_day_coverage(self):
        """
        Run the function multiple times and ensure that all months appear at least once.
        """
        months_generated = {get_lucky_day().split(' ')[-1].split('/')[0] for _ in range(100)}
        expected_months = {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}
        

        assert expected_months.issubset(months_generated), "The function should generate all months over multiple runs."


    #positive action tests

    # Test 1: Ensure the function returns a non-empty string
    def test_get_positive_message_non_empty(self):
        """
        Verify that get_positive_message() returns a non-empty string.
        """
        result = get_positive_action()
        
        assert isinstance(result, str), "The result should be a string."
        assert len(result) > 0, "The result should not be an empty string."

    # Test 2: Ensure the output contains both a positive message and a suggestion
    def test_get_positive_message_structure(self):
        """
        Verify that get_positive_message() contains both a positive message and a suggestion in the output.
        """
        result = get_positive_action()
        
        assert "Today's Positive Message: '" in result, "The result should contain the label for the positive message."
        assert "Suggestion: " in result, "The result should contain the label for the suggestion."

    # Test 3: Ensure the function outputs different results for uniqueness
    def test_get_positive_message_uniqueness(self):
        """
        Run get_positive_message() multiple times and check for output uniqueness.
        """
        results = {get_positive_action() for _ in range(10)}
        assert len(results) > 1, "The function should generate unique positive messages and suggestions."



    #answers of wisdom tests