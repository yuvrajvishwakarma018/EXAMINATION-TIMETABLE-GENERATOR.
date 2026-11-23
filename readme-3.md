# Examination Timetable Generator

**Project No.:** PS 89  
**Project Title:** Examination Timetable Generator  
**Course:** Bachelor of Computer Application  
**Language:** Python 3

## 1. Problem statement
Generate an examination date sheet from an ordered list of subjects, a start date, and optional holiday dates. Schedule exactly one exam per day, preserve the subject order, and skip Sundays and supplied holidays.

## 2. Requirements
- Accept a list of subjects, a start date, and optional holiday dates.
- Validate date input in `DD-MM-YYYY` format.
- Reject an empty subject list.
- Reject duplicate subject names.
- Reject invalid calendar dates.
- Use a list for subjects and dictionaries for date-sheet entries.
- Schedule one subject per eligible day, preserving the input order.
- Skip Sundays and dates listed as holidays.

## 3. How to run
1. Install Python 3.
2. Keep `code.py` in this folder.
3. Open a terminal in this folder.
4. Run:

```bash
python3 code.py
```

5. Enter subjects in the order requested by the program, the start date, and holiday dates (if any).

## 4. Input format
- Subjects: comma-separated names, for example `DAA, DBMS, OOP, Maths, CSA`
- Start date: `DD-MM-YYYY`, for example `12-10-2026`
- Holidays: comma-separated dates in `DD-MM-YYYY`; enter `none` if there are no holidays.

## 5. Test cases
See `testcases.pdf` for the four test cases and expected results from the project allocation sheet. `sample_inputs.txt` contains the same cases in a convenient console-input format.

## 6. Important reference
The project allocation sheet states that 12-10-2026 is Monday and 18-10-2026 is Sunday. The expected outputs below follow that reference.

## 7. Submission files
- `code.py` — implementation (maintained separately by the student)
- `readme.md` — this documentation
- `testcases.pdf` — test cases and expected outputs
- `sample_inputs.txt` — sample test inputs
- `project_allocation_image.jpeg` — supplied project allocation page
