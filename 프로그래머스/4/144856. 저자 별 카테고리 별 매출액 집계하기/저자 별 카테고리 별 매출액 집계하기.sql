-- 코드를 입력하세요
SELECT AUTHOR_ID,AUTHOR_NAME, CATEGORY, SUM(PRICE*SALES) TOTAL_SALES
FROM (SELECT * FROM BOOK_SALES WHERE SALES_DATE BETWEEN '20220101' and '20220131') S
 LEFT OUTER JOIN (
        SELECT B.BOOK_ID, A.AUTHOR_ID, B.PRICE, A.AUTHOR_NAME, B.CATEGORY
          FROM BOOK B
        INNER JOIN AUTHOR A
        ON B.AUTHOR_ID = A.AUTHOR_ID
    ) INFO
 ON INFO.BOOK_ID = S.BOOK_ID
 GROUP BY AUTHOR_ID, CATEGORY -- INFO.BOOK_ID
 ORDER BY AUTHOR_ID ASC, CATEGORY DESC
# SELECT * FROM BOOK
# INNER JOIN AUTHOR
# ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID