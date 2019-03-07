Feature: Amazon search capability

    Scenario: Search for a blender
        Given we are at www.amazon.com
        When we search for blender
        Then we will get at least 20 results
         and 75% of the results will contain blender

    Scenario: Search for a mixer
        Given we are at www.amazon.com
        When we search for mixer
        Then we will get at least 20 results
         and 75% of the results will contain mixer

    Scenario: Search for a toaster
        Given we are at www.amazon.com
        When we search for toaster
        Then we will get at least 20 results
         and 75% of the results will contain toaster