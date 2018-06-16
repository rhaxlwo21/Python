from datetime import datetime

t = ['월','화','수','목','금','토','일',]
r = datetime.today().weekday()

sub = t[r] + "요일 시간표\n"
bar = "==========\n"
danger = "변경된 시간표는 책임지지 않습니다"

if t[r] == "월":
    classTime = "1 . 물리\n2. 생물\n3. 미적\n4. 미술\n5. 영A\n6. 문A\n7. 문C\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "화":
    classTime = "1 . 미적\n2. 영A\n3. 문B\n4. 일본어/중국어\n5. 체육A\n6. 진로\n7. 화학\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "수":
    classTime = "1 . 지구과학\n2. 문A\n3. 물리\n4. 미술\n5. 일본어/중국어\n6. 미적A\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "목":
    classTime = "1 . 체육\n2. 일본어/중국어\n3. 미적\n4. 영B\n5. 미적\n6. 지구과학\n7. 문B\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "금":
    classTime = "1 . 미적\n2. 화확\n3. 생물\n4. 영A\n5. 창체\n6. 창체\n"
    class26 = sub + bar + classTime + bar + danger
elif t[r] == "토" or "일":
    classTime = "토,일요일은 수업이 없습니다\n"
    class26 = sub + bar + classTime + bar + danger
