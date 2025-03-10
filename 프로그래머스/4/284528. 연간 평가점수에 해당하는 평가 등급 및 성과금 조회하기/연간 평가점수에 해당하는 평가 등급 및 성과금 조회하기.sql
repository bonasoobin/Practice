SELECT G.EMP_NO, E.EMP_NAME, 
       CASE WHEN AVG(G.SCORE) >= 96 THEN 'S'
            WHEN AVG(G.SCORE) >= 90 AND AVG(G.SCORE) < 96 THEN 'A'
            WHEN AVG(G.SCORE) >= 80 AND AVG(G.SCORE) < 90 THEN 'B'
            ELSE 'C' END GRADE, 
        CASE WHEN AVG(G.SCORE) >= 96 THEN E.SAL * 0.2
             WHEN AVG(G.SCORE) >= 90 AND AVG(G.SCORE) < 96 THEN E.SAL * 0.15
             WHEN AVG(G.SCORE) >= 80 AND AVG(G.SCORE) < 90 THEN E.SAL * 0.1
             ELSE 0 END BONUS
FROM HR_DEPARTMENT D JOIN HR_EMPLOYEES E ON D.DEPT_ID = E.DEPT_ID JOIN HR_GRADE G ON E.EMP_NO = G.EMP_NO
GROUP BY G.EMP_NO
ORDER BY G.EMP_NO;