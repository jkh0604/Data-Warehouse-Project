INSERT INTO students (AcademicID, CollegeID, SemesterID)
SELECT a.AcademicID, p.CollegeID, t.SemesterID
FROM academics a, program p, time t, staging s
WHERE a.AcademicID = s.ID 
	AND p.Major = s.Major AND p.Degree = s.Degree
    AND t.MonthDay = s.MonthDay AND t.Y = s.Y;
