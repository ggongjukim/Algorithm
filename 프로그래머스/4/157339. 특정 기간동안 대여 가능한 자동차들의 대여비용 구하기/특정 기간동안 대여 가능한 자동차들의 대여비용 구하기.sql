-- 코드를 입력하세요
# SELECT * FROM CAR_RENTAL_COMPANY_CAR WHERE CAR_ID IN (27,18)
#SELECT * FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY WHERE CAR_ID IN (27,18) and END_DATE < '20221101'
# SELECT * FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN -- 세단 8 suv 5

# SELECT A.CAR_ID, A.CAR_TYPE, 
#     ROUND(A.DAILY_FEE * (1- (B.DISCOUNT_RATE / 100)) * 30, 0) AS FEE
#     ,A.START_DATE, A.END_DATE
# FROM 
# (SELECT R.CAR_ID, R.CAR_TYPE, R.DAILY_FEE,H.START_DATE, H.END_DATE
#       FROM CAR_RENTAL_COMPANY_CAR R
#           LEFT OUTER JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
#           ON R.CAR_ID = H.CAR_ID 
#           WHERE H.END_DATE < '20221101' -- OR H.START_DATE > '20221201' 
#           and R.CAR_TYPE in ('SUV', '세단')) A
#       LEFT OUTER JOIN (SELECT * FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN P WHERE P.DURATION_TYPE = '30일 이상') B
#       ON A.CAR_TYPE = B.CAR_TYPE

# WHERE A.DAILY_FEE * (1 - (B.DISCOUNT_RATE / 100)) * 30 >= '500000'
# and A.DAILY_FEE * (1 - (B.DISCOUNT_RATE / 100)) * 30 <= '2000000'
# # GROUP BY CAR_ID
# ORDER  BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC


SELECT A.CAR_ID, A.CAR_TYPE, ROUND(A.DAILY_FEE * (1- (P.DISCOUNT_RATE / 100)) * 30, 0) AS FEE
    # ,A.DAILY_FEE
FROM CAR_RENTAL_COMPANY_CAR AS A 
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P
ON A.CAR_TYPE = P.CAR_TYPE
WHERE 
    A.CAR_TYPE IN ('세단', 'SUV')
    AND P.DURATION_TYPE = '30일 이상'
    AND A.DAILY_FEE * (1 - (P.DISCOUNT_RATE / 100)) * 30 BETWEEN 500000 AND 2000000
    AND A.CAR_ID NOT IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE END_DATE >= '2022-11-01' AND START_DATE < '2022-12-01'
)
ORDER BY FEE DESC, A.CAR_TYPE, A.CAR_ID DESC -- 3 23