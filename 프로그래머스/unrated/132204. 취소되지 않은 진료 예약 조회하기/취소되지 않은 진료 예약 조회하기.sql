-- 코드를 입력하세요
SELECT a.apnt_no, p.pt_name, p.pt_no, d.mcdp_cd, d.dr_name, a.apnt_ymd
from  doctor d, appointment a, patient p
where 1=1 
        AND a.MDDR_ID = d.DR_ID
        AND a.MCDP_CD = d.MCDP_CD
        AND a.PT_NO = p.PT_NO
        AND a.APNT_CNCL_YN = 'N'
        AND a.MCDP_CD = 'CS'
        AND TO_CHAR(a.APNT_YMD,'YYYYMMDD') = '20220413'
order by a.apnt_ymd;
