// Helper functions for music
#include <string.h>
#include <cs50.h>
#include <math.h>
#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    int a = 0;
    if(fraction[0] == '1')
    {
        if(fraction[2] == '8')
        {
            a = 1;
        }
        else if(fraction[2] == '4')
        {
            a = 2;
        }
        else if(fraction[2] == '2')
        {
            a = 4;
        }
        else if(fraction[2] == '1')
        {
            a = 8;
        }
    }
    else if(fraction[0] == '3' && fraction[2] == '8')
    {
        a = 3;
    }
    else
    {
        a = 0;
    }
    return a;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    int octave = (int)note[(strlen(note))-1];
    double freq;

    octave = octave - 48;   // das hier ist noch zur Überlegung


    switch(note[0])
    {
        case 'C':
        {
            freq = 440.0 * (pow(2.0, (-9.0/12.0)));
            break;
        }
        case 'D':
        {
            freq = 440.0 * (pow(2.0, (-7.0/12.0)));
            break;
        }
        case 'E':
        {
            freq = 440.0 * (pow(2.0, (-5.0/12.0)));
            break;
        }
        case 'F':
        {
            freq = 440.0 * (pow(2.0, (-4.0/12.0)));
            break;
        }
        case 'G':
        {
            freq = 440.0 * (pow(2.0, (-2.0/12.0)));
            break;
        }
        case 'A':
        {
            freq = 440.0 * (pow(2.0, (0.0/12.0)));
            break;
        }
        case 'B':
        {
            freq = 440.0 * (pow(2.0, (2.0/12.0)));
            break;
        }
        default:
        {
            return 0;
        }
    }

    if (octave > 4)
    {
        freq = freq * 2 * (octave - 4);
    }
    if (octave < 4)
    {
        freq = freq / (2 * (4 - octave));
    }
    if(note[1] == 'b')
    {
        freq = freq * (pow(2.0, (-1.0 / 12.0)));
    }
    else if(note[1] == '#')
    {
        freq = freq * (pow(2.0, (1.0 / 12.0)));
    }

    int frequency = round(freq);
    return frequency;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (strcmp(s, "") == 0)
    {
        return true;
    }
    else
        return false;
}
