#include <iostream>

using namespace std;

int main()
{
    string  roman;
    int num = 0;
    string s = "iii";
    

    for (int i = 0; i < s.length(); i++)
    {
        roman += toupper(s[i]);
    }

    switch (s.length())
    {
    case 1:
        if (roman == "I")
        {
            num += 1;
            break;
        }
        if (roman == "V")
        {
            num += 5;
            break;
        }
        if (roman == "L")
        {
            num += 50;
            break;
        }
        if (roman == "X")
        {
            num += 10;
            break;
        }
        if (roman == "C")
        {
            num += 100;
            break;
        }
        if (roman == "M")
        {
            num += 1000;
            break;
        }
        if (roman == "D")
        {
            num += 500;
            break;
        }
        break;

    default:
        for (int i = 0; i < s.length(); i++)
        {
            if (roman[i] == 'I')
            {
                if (roman[i + 1] == 'V' || roman[i + 1] == 'X' || roman[i + 1] == 'L' || roman[i + 1] == 'C' || roman[i + 1] == 'D' || roman[i + 1] == 'M')
                {
                    num += 0;
                }
                else
                {
                    num += 1;
                }
            }

            if (roman[i] == 'V')
            {
                if (roman[i + 1] == 'X' || roman[i + 1] == 'L' || roman[i + 1] == 'C' || roman[i + 1] == 'D' || roman[i + 1] == 'M')
                {
                    num += 0;
                }
                else
                {
                    if (roman[i - 1] == 'I')
                    {
                        num -= 1;
                    }

                    num += 5;
                }
            }

            if (roman[i] == 'X')
            {
                if (roman[i + 1] == 'L' || roman[i + 1] == 'C' || roman[i + 1] == 'D' || roman[i + 1] == 'M')
                {
                    num += 0;
                }
                else
                {
                    if (roman[i - 1] == 'I')
                    {
                        num -= 1;
                    }
                    if (roman[i - 1] == 'V')
                    {
                        num -= 5;
                    }

                    num += 10;
                }
            }

            if (roman[i] == 'L')
            {
                if (roman[i + 1] == 'C' || roman[i + 1] == 'D' || roman[i + 1] == 'M')
                {
                    num += 0;
                }
                else
                {
                    if (roman[i - 1] == 'X')
                    {
                        num -= 10;
                    }

                    if (roman[i - 1] == 'V')
                    {
                        num -= 5;
                    }
                    if (roman[i - 1] == 'I')
                    {
                        num -= 1;
                    }
                    num += 50;
                }
            }

            if (roman[i] == 'C')
            {
                if (roman[i + 1] == 'D' || roman[i + 1] == 'M')
                {
                    num += 0;
                }
                else
                {
                    if (roman[i - 1] == 'L')
                    {
                        num -= 50;
                    }
                    if (roman[i - 1] == 'X')
                    {
                        num -= 10;
                    }
                    if (roman[i - 1] == 'V')
                    {
                        num -= 5;
                    }
                    if (roman[i - 1] == 'I')
                    {
                        num -= 1;
                    }

                    num += 100;
                }
            }

            if (roman[i] == 'D')
            {
                if (roman[i + 1] == 'M')
                {
                    num += 0;
                }
                else
                {
                    if (roman[i - 1] == 'I')
                    {
                        num -= 1;
                    }
                    if (roman[i - 1] == 'V')
                    {
                        num -= 5;
                    }
                    if (roman[i - 1] == 'X')
                    {
                        num -= 10;
                    }
                    if (roman[i - 1] == 'L')
                    {
                        num -= 50;
                    }
                    if (roman[i - 1] == 'C')
                    {
                        num -= 100;
                    }
                    num += 500;
                }
            }

            if (roman[i] == 'M')
            {
                if (roman[i - 1] == 'I')
                {
                    num -= 1;
                }
                if (roman[i - 1] == 'V')
                {
                    num -= 5;
                }
                if (roman[i - 1] == 'X')
                {
                    num -= 10;
                }
                if (roman[i - 1] == 'L')
                {
                    num -= 50;
                }
                if (roman[i - 1] == 'C')
                {
                    num -= 100;
                }
                if (roman[i - 1] == 'D')
                {
                    num -= 500;
                }
                num += 1000;
            }
        }
    }

    cout<<num;
    return 0;
}