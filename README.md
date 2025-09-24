# **[Velog Dashboard V2](https://velog-dashboard.kro.kr/)**

<img width="1200" height="800" alt="68747470733a2f2f76656c6f672d64617368626f6172642e6b726f2e6b722f6f70656e67726170682d696d6167652e706e67" src="https://github.com/user-attachments/assets/e9bccd60-a17d-45fb-b675-57495ba7aa72" />
<img width="1200" height="800" alt="스크린샷 2025-09-24 오전 9 06 38" src="https://github.com/user-attachments/assets/72a920f6-94db-49e6-8432-bc1492e4ee19" />
<img width="1200" height="800" alt="스크린샷 2025-09-24 오전 9 06 50" src="https://github.com/user-attachments/assets/e35a3d9b-a504-4054-a720-2637a75f366f" />
<img width="1200" height="1000" alt="68747470733a2f2f76656c6f672e76656c63646e2e636f6d2f696d616765732f716c676b73312f706f73742f63366537643066312d306334332d343831612d393936352d3533613239653461376537302f696d6167652e706e67" src="https://github.com/user-attachments/assets/0fe2c918-1f33-4670-ab0f-7e980e0aafe8" />

<br /><br />

## 1. 프로젝트 개요
Velog 게시글 및 사용자 데이터를 수집/분석하여 대시보드 형태로 제공하는 프로젝트입니다.  
주간 트렌드 분석, 사용자 게시글 분석, 그리고 PLG 스택(Prometheus, Loki, Grafana, Alloy)을 통한 모니터링 환경을 구축했습니다.
<br /><br />

## 2. 아키텍처 다이어그램
<img width="2055" height="1002" alt="image" src="https://github.com/user-attachments/assets/9633d0d2-1946-473b-98c1-5e3c3a13cffa" />
<br /><br />

## 3. 팀원 - 현재 4인 팀
<table>
  <tr>
    <td align="center" width="96">
      <img src="https://avatars.githubusercontent.com/u/33516349?v=4" width="48" height="48" alt="nuung" />
      <br>
      <i><a href="https://github.com/nuung">Nuung</a></i>
    </td>
    <td align="center" width="96">
      <img src="https://avatars.githubusercontent.com/u/107257423?v=4" width="48" height="48" alt="six-standard" />
      <br>
      <i><a href="https://github.com/six-standard">six-standard</a></i>
    </td>
    <td align="center" width="96">
      <img src="https://avatars.githubusercontent.com/u/105155269?v=4" width="48" height="48" alt="Jihyun3478" />
      <br>
      <i><a href="https://github.com/Jihyun3478">Jihyun3478</a></i>
    </td>
  </tr>
  <tr>
    <td align="center" width="96">
      <img src="https://avatars.githubusercontent.com/u/146878715?s=64&v=4" width="48" height="48" alt="ooheunda" />
      <br>
      <i><a href="https://github.com/ooheunda">ooheunda</a></i>
    </td>
    <td align="center" width="96">
      <img src="https://avatars.githubusercontent.com/u/154482801?v=4" width="48" height="48" alt="HA0N1" />
      <br>
      <i><a href="https://github.com/HA0N1">HA0N1</a></i>
    </td>
    <td align="center" width="96">
      <img src="https://avatars.githubusercontent.com/u/88363672?v=4" width="48" height="48" alt="BDlhj" />
      <br>
      <i><a href="https://github.com/BDlhj">BDlhj</a></i>
    </td>
  </tr>
</table>

<br /><br />

## 4. 프로젝트 정보
### 1️⃣ 어떤 개발을
- Velog 트렌딩 게시글 데이터 수집 및 분석 배치 구현, 모니터링 대시보드 구축

### 2️⃣ 어떤 기술 스택으로
- Python 3, Django 5, PostgreSQL, Docker
- Prometheus, Grafana, Loki, Alloy (PLG Stack)
- Pytest, Velog API, OpenAI API

### 3️⃣ 얼마동안
- 2025.02 ~ 진행 중 (약 7개월)

### 4️⃣ 목표 달성 여부
- Velog API 기반 트렌딩 게시글 수집 및 저장  
- 관리자 페이지 최적화 (쿼리 N+1 문제 해결 → 응답속도 8s → 0.7s 단축)  
- PLG 스택 기반 모니터링 환경 구축 및 운영 지표 시각화  
- Django 비동기 배치 + OpenAI API 기반 주간 트렌드 분석 자동화

### 5️⃣ 기여도
- 관리자 페이지 최적화 및 DB 인덱싱 → QPS 1,100 → 1~3 (99% 개선), 응답속도 7.5s → 0.7s  
- PLG 스택 설치 및 Alloy 로그 수집 파이프라인 구성  
- 주간 사용자 분석 및 트렌드 분석 배치 코드 작성 (LLM 기반 요약/통계 반영)  
- 테스트 코드(Pytest)로 데이터 정합성 및 안정성 검증  

<br /><br />

## 5. 성과
- 관리자 페이지 조회 쿼리: 1,100회 → 2회 (99% 개선)  
- 관리자 페이지 응답 시간: 7.5초 → 0.7초 (90% 단축)  
- 운영 지표 대시보드 구축 → 장애 탐지 시간 30분 → 2분 단축
