public static int longRepeat(String text) {

    int longCount = 0;
    char curChar = '';
    int curCount = 0;

    /*

    Students might also use regular for loop, e.g.:

    for (int i = 0; i < text.length(); i++) {
    }

    In which case they'll need to access the current character
    via the String.charAt() method or similar technique.

    */

    for (char letter : text.toCharArray())
    {

        if (letter == curChar)
        {
            curCount++;
        }
        else
        {
            curChar = char;
            curCount = 1;
        }

        if curCount > longCount {
            longCount = curCount;
        }

    }

    

    return longCount;
    
}