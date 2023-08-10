# [학습자료] 데이터 사이언스와 시각화

## 목차

1. 데이터 사이언스 개요\_데이터 분석 맛보기
2. [데이터 사이언스 개요\_분석 환경 준비하기](#2-데이터-사이언스-개요_분석-환경-준비하기)
3. [데이터 조작 이해와 실무\_데이터 선택](#3-데이터-조작-이해와-실무\_데이터-선택)
4. [데이터 조작 이해와 실무\_데이터 변경](#4-데이터-조작-이해와-실무\_데이터-변경)
5. [데이터 조작 이해와 실무\_데이터 합치기](#5-데이터-조작-이해와-실무\_데이터-합치기)
6. [데이터 조작 이해와 실무\_데이터 그룹핑](#6-데이터-조작-이해와-실무\_데이터-그룹핑)
7. [데이터 조작 이해와 실무\_시계열 데이터 기초](#7-데이터-조작-이해와-실무\_시계열-데이터-기초)
8. [데이터 전처리 이해와 실무\_데이터 정제 – 결측 데이터 처리](#8-데이터-전처리-이해와-실무\_데이터-정제---결측-데이터-처리)
9. [데이터 전처리 이해와 실무\_데이터 정체 – 이상 데이터 처리](#9-데이터-전처리-이해와-실무\_데이터-정체---이상-데이터-처리)
10. [데이터 전처리 이해와 실무\_데이터 변환 – 정규화, 구간화](#10-데이터-전처리-이해와-실무\_데이터-변환---정규화,-구간화)
11. [데이터 전처리 이해와 실무\_데이터 변환 – 특징 생성](#11-데이터-전처리-이해와-실무\_데이터-변환---특징-생성)
12. [데이터 전처리 이해와 실무\_데이터 축소 – 특징 선택](#12-데이터-전처리-이해와-실무\_데이터-축소---특징-선택)
13. [데이터 탐색 이해와 실무\_일변량 비시각화 탐색](#13-데이터-탐색-이해와-실무\_일변량-비시각화-탐색)
14. [데이터 탐색 이해와 실무\_일변량 시각화 탐색](#14-데이터-탐색-이해와-실무\_일변량-시각화-탐색)
15. [데이터 탐색 이해와 실무\_다변량 비시각화 탐색](#15-데이터-탐색-이해와-실무\_다변량-비시각화-탐색)
16. [데이터 탐색 이해와 실무\_다변량 시각화 탐색](#16-데이터-탐색-이해와-실무\_다변량-시각화-탐색)
17. [데이터 분석 이해와 실무\_가설의 의의와 검정](#17-데이터-분석-이해와-실무\_가설의-의의와-검정)
18. [데이터 분석 이해와 실무\_상관 분석](#18-데이터-분석-이해와-실무\_상관-분석)
19. [데이터 분석 이해와 실무\_회귀 분석](#19-데이터-분석-이해와-실무\_회귀-분석)
20. [데이터 분석 이해와 실무\_시계열 분석](#20-데이터-분석-이해와-실무\_시계열-분석)
21. [데이터 시각화 이해와 실무\_정적 시각화 개요](#21-데이터-시각화-이해와-실무\_정적-시각화-개요)
22. [데이터 시각화 이해와 실무\_정적 시각화 실습 – matplotlib 활용](#22-데이터-시각화-이해와-실무\_정적-시각화-실습---matplotlib-활용)
23. [데이터 시각화 이해와 실무\_정적 시각화 실습 – seaborn 활용](#23-데이터-시각화-이해와-실무\_정적-시각화-실습---seaborn-활용)
24. [데이터 시각화 이해와 실무\_동적 시각화 개요](#24-데이터-시각화-이해와-실무\_동적-시각화-개요)
25. [데이터 시각화 이해와 실무\_동적 시각화 실습 – plotly 활용](#25-데이터-시각화-이해와-실무\_동적-시각화-실습---plotly-활용)
26. [데이터 시각화 이해와 실무\_UI 시각화 실습 – streamlit 활용](#26-데이터-시각화-이해와-실무\_UI-시각화-실습---streamlit-활용)


## 2. 데이터 사이언스 개요\_분석 환경 준비하기

### - 특정 파이썬 버전으로 새로운 conda 가상 환경 생성

```
conda create --name [ENV_NAME] python=[PYTHON_VERSION]
```

### - 모든 conda 환경들을 나열

```
conda info --envs
```

### - conda 환경 활성화 / 현재 conda 환경 비활성화

```
conda activate [ENV_NAME]
conda deactivate
```

### - 현재 conda 환경에 Jupyter Notebook 설치

```
conda install jupyter notebook
```

### - 현재 conda 환경에 특정 패키지 설치

```
conda install [PACKAGE_NAME]
```

### - conda 환경을 Jupyter Notebook에 등록

```
python -m ipykernel install --user --name [ENV_NAME] --display-name "[DISPLAY_NAME]"
```

### - Jupyter Notebook 시작

```
jupyter notebook
```

### - 기존 환경을 복제하여 새로운 conda 환경 생성

```
conda create --name [NEW_ENV_NAME] --clone [EXISTING_ENV_NAME]
```

### - conda 환경 제거

```
conda env remove --name [ENV_NAME]
```

### - 현재 conda 환경을 YAML 파일로 내보내기

```
conda env export > [ENV_NAME].yaml
```

### - YAML 파일로부터 새로운 conda 환경 생성

```
conda env create --file [ENV_NAME].yaml
```

## 3. 데이터 조작 이해와 실무\_데이터 선택

### - Numpy: Python에서 수치 계산을 위한 핵심 라이브러리. 대규모 다차원 배열 및 행렬 연산에 필요한 다양한 함수를 제공하며, 이는 고성능의 수학 연산과 과학 연산 작업에 필수적.

#### 주요 특징

1. 다차원 배열 객체: NumPy의 핵심 기능은 ndarray라는 다차원 배열 객체.
2. 브로드캐스팅: 다른 크기의 배열 간 연산을 지원하는 기능.
3. 통합 수학 함수: 배열 데이터를 처리하는 데 필요한 기본적인 수학 함수를 제공.
4. 선형 대수, 난수 생성, 푸리에 변환과 같은 고급 수학 및 통계 연산 지원.
5. C, C++, 포트란과 같은 저수준 언어로 작성된 코드와 통합이 가능.

### - Pandas: Python에서 데이터 분석을 위한 가장 인기 있는 라이브러리. 고성능의 DataFrame 객체를 제공하여 데이터 분석, 클린징, 처리, 시각화 등의 작업을 효과적으로 수행 가능.

#### 주요 특징

1. 데이터 구조: Series와 DataFrame이라는 두 가지 주요 데이터 구조를 제공.
2. Series: 1차원 배열과 같은 데이터 구조로, 여러 데이터 타입을 저장할 수 있음.
3. DataFrame: 2차원 레이블이 있는 데이터 구조로, 다양한 타입의 열을 가질 수 있음.
4. 데이터 처리: 데이터 병합, 조인, 리쉐이핑, 피벗, 슬라이싱, 인덱싱, 데이터 클린징 등의 다양한 데이터 처리 기능을 제공.
5. 데이터 분석: 그룹화, 집계, 통계 계산 등의 기능을 통해 데이터 분석을 지원.
6. 시계열 처리: 날짜 및 시간 데이터를 위한 기능을 제공하며, 시계열 분석 및 빈도 변환 등의 작업을 수행 가능.
7. 데이터 입출력: CSV, Excel, SQL, HDF5, Parquet 등 다양한 데이터 소스로부터 데이터를 읽고 쓸 수 있는 기능을 제공.

## 4. 데이터 조작 이해와 실무\_데이터 변경

### - 주어진 data로부터 데이터프레임을 생성

```python
pandas.DataFrame(data):
```

### - 주어진 데이터프레임에 다른 데이터프레임, 시리즈, 딕셔너리, 배열을 추가

```python
DataFrame.append(data, ignore_index=True):
```

### - 특정 인덱스의 특정 열 값에 빠르게 접근

```python
DataFrame.at[index, 'column_name']:
```

### - 특정 인덱스(행)을 제거한 새로운 데이터프레임을 반환

```python
DataFrame.drop(index)
```

### - 특정 열을 제거한 새로운 데이터프레임을 반환

```python
DataFrame.drop(columns=column_name)
```

### - 특정 열을 데이터프레임의 인덱스로 설정

```python
DataFrame.set_index(column_name, drop=True)
```

## 5. 데이터 조작 이해와 실무\_데이터 합치기

### - 데이터 병합: 각기 다른 두 개 이상의 Dataframe을 하나로 병합하여 결과 집합을 만들어 내는 것.

- Inner Join: Dataframe 간 조인 조건을 만족하는 행을 합치는 것.

1. One-to-One
2. One-to-Many

- Outer Join: 조건에 부합하지 않는 행까지 포함시켜 결합하는 방법. NaN 처리를 함.
- Left Join: 첫 번째 Dataframe을 기준으로 두 번째 Dataframe을 결합하는 방법.
- Right Join: 첫 번째 Dataframe을 기준으로 첫 번째 Dataframe을 결합하는 방법.

### - join

- 인덱스를 기준으로 함.
- DataFrame의 메소드로 사용함.
- 왼쪽 DataFrame을 기준으로함.
- 중복된 칼럼이 있다면, 두 개 칼럼 모두 Dataframe에 다른 이름올 저장됨.

### - Merge

- 열을 기준으로 함.
- Pandas의 함수로 사용함.
- 기본적으로 inner join. how 파라미터를 통해 변경 가능.

### - Concatenate

- 연결은 공유하는 Key 값을 사용하지 않고, 데이터를 기존 DataFrame 아래(또는 우측)에 붙여 연결함.

## 6. 데이터 조작 이해와 실무\_데이터 그룹핑

### - groupby: 특정 열, 열의 리스트 또는 행 인덱스를 기준으로 그룹화를 진행함.
- count: 각 그룹의 각 열의 누락되지 않은 값의 개수를 세어줌.
- sum: 각 그룹의 각 열의 합계를 구해줌.
- mean: 각 그룹의 각 열의 평균값을 구해줌.
- median: 각 그룹의 각 열의 중앙값을 구해줌.
- min: 각 그룹의 각 열의 최솟값을 구해줌.
- max: 각 그룹의 각 열의 최댓값을 구해줌.
- var: 각 그룹의 각 열의 분산을 구해줌.
- std: 각 그룹의 각 열의 표준편차를 구해줌.
- first: 각 그룹의 각 열의 첫 번째 값 (누락되지 않은)을 가져옴.
- last: 각 그룹의 각 열의 마지막 값 (누락되지 않은)을 가져옴.
- describe: 각 그룹의 각 열의 기술통계량을 계산하여 반환함. (평균, 표준편차, 최소값, 최대값 등)
- aggregate 또는 agg: 사용자가 지정한 하나 이상의 연산을 각 그룹의 각 열에 적용함. 집계 함수의 리스트나 딕셔너리를 전달할 수 있음.
- apply: 각 그룹의 각 열에 함수를 적용하고, 결과를 합쳐줌. 매우 유연하며 사용자 정의 함수를 사용할 수 있음.

### - sort_values
- 형태
```python
dataframe.sort_values(by='열이름')
```

- 옵션
1. by: 정렬할 기준이 되는 열의 이름 또는 열의 이름 리스트를 지정. 여러 열을 리스트로 전달하면, 순차적으로 정렬됨.
2. axis: 정렬을 수행할 축을 지정. 0은 행 기준, 1은 열 기준. 기본값은 0입니다.
3. ascending: 정렬 순서를 지정. True이면 오름차순, False이면 내림차순. 여러 열을 정렬할 때는 불리언 값의 리스트를 전달할 수 있음. 기본값은 True.
4. inplace: 원본 객체를 변경할지 여부를 지정. True이면 원본 객체가 변경되고, False이면 새로운 객체가 반환됨. 기본값은 False.
5. na_position: 결측값(NaN)의 위치를 지정. 'first'이면 결측값이 처음에 위치하고, 'last'이면 마지막에 위치합. 기본값은 'last'.
6. ignore_index: 인덱스를 재설정할지 여부를 지정. True이면 인덱스가 재설정되고, False이면 원본 인덱스가 유지됨. 기본값은 False.

## 7. 데이터 조작 이해와 실무\_시계열 데이터 기초

### - 시계열 데이터: 순차적인 시간의 흐름으로 기록된 관측치의 집합
* 시간이 순차적인 경우에 사용.
* 고정된 시간 구간의 관측치: 시간 구간이 일정해야함.
* DatetimeIndex라는 자료형을 사용함.

### - 시간 그래프(Time Plot): 패턴, 이상치, 시간에 따른 변화, 계절성 등의 데이터의 많은 특징을 눈으로 볼 수 있게 해줌.

### - 문자열을 datetime으로 변환
```python
pandas.to_datetime() 
```

### - 데이터를 특정 방향으로 이동시키는 기능을 제공.
```python
shift()
```

### - 시계열 데이터에서 각 요소 간의 차이를 계산하는 기능을 제공
```python
diff()
```

### - Resampling
#### 다운샘플링: 원래의 데이터가 그룹으로 묶여 대표값 필요. 데이터의 양이 감소.
#### 업샘플링: 실제로 존재하지 않는 데이터를 만듦. 데이터의 값이 증가.
##### Forward filling: 처음 데이터를 기준으로 결측치를 보관함.
- 시계열 데이터에서 값이 연속적으로 유지되어야 할 때.
- 센서로부터의 읽기 누락 등이 있어 직전 데이터를 현재 값으로 사용해야 할 때.

##### Backward filling: 마지막 데이터를 기준으로 결측치를 보관함.
- 미래의 데이터가 과거의 누락된 값에 더 영향을 미칠 것으로 예상되는 상황.
- 특정 이벤트 후의 데이터가 더 중요한 정보를 제공할 수 있을 때.

## 8. 데이터 전처리 이해와 실무\_데이터 정제 - 결측 데이터 처리

### - 제거하기: 데이터 손실 발생.
- Likewise deletion: 결측치가 존재하는 행 삭제.
- Pairwise deletion: 모든 변수가 결측치로만 존재하는 행 삭제.

### - 대체하기: 편향(Bias) 발생 가능. 정보의 손실을 방지하나 변수 특성(평균, 상관관계)에 영향 발생.
- 일정 값 대체
- 선형 값 대체
1. linear(기본값): 선형 보간을 수행하여 결측값을 주변 두 값의 선형 비율에 따라 추정.
2. time: 시계열 데이터에서 사용할 때, 시간에 따른 선형 보간을 수행.
3. polynomial: 다항식 보간을 수행.
4. spline: 스플라인(spline) 보간을 수행.

## 9. 데이터 전처리 이해와 실무\_데이터 정체 - 이상 데이터 처리

### - Z-score
- 데이터가 평균에서 얼마나 떨어져 있는지를 표준편차의 단위로 나타내는 값.
- 평균으로부터 얼마나 떨어져 있는지를 알 수 있으므로 데이터가 평균으로부터 얼마나 표준편차만큼 떨어져 있는지를 측정하는 표준화된 값으로 사용됨.
- Z = (X - μ) / σ
1. X: 개별 데이터 포인트 값.
2. μ: 데이터의 평균.
3. σ: 데이터의 표준편차.

### - IQR(Interquartile Range)
* 데이터의 중간 50% 범위를 나타내는 값.
* 데이터의 중간 50% 범위를 간단하게 측정하는 방법.
* IQR = Q3 - Q1
1. Q3: 75% 지점
2. Q1: 25% 지점

## 10. 데이터 전처리 이해와 실무\_데이터 변환 - 정규화, 구간화

### - Transformation: 여러 형태로 표현된 데이터 값을 다양한 분석 방법론에 적용하기 위해 원시 형태에서 다른 형식으로 바꾸는 과정
- 목적 및 특징
1. 빠른 특성 파악
2. 분석 알고리즘 적용: 다른 범위를 지닌 변수들의 변환 필요

### 구간화(Binning): 데이터를 더 쉽게 이해하고 분석할 수 있게 도와줌. 연속형 데이터를 구간으로 구별하여 범주화 형태 변환.
- 특징
1. 지정 길이 기반 구간 정의: 직접 구간의 크기를 정해서 나누는 방법. 사용자 기준으로 데이터 범위의 간격을 구분하여 관측치를 나눔.
2. 분포 기간 구간 정의: 모든 구간에 같은 개수의 숫자가 들어가도록 나누는 것. 관측치가 각 구간 내 동일한 개수로 구분되도록 나눔.

### 정규화: 데이터 탐색 및 기계학습 적용을 위한 연속형 변수 변환.
- 최대-최소 정규화
1. 데이터 구간을 0에서 1사이로 변환. 데이터의 위치 파악.
2. 이상치에 민감할 수 있는 단점.
3. X(normalized) = (X - X(min)) / (X(max) - X(min))
- Z-점수 정규화(표준화)
1. 0을 중심으로 양쪽으로 데이터 분포시킴.
2. 특정 데이터가 평균화 얼마나 떨어져 있는지 파악.
3. Z = (X - μ(평균)) / a(표준편차)

## 11. 데이터 전처리 이해와 실무\_데이터 변환 - 특징 생성

### Feature Creation: 원본 데이터의 조합/변환 등을 기반하여 새로운 특징들을 구축 및 생성하는 방법

### 목적 및 필요성
- 품질 확보: 가공을 거치지 않은 Raw 데이터 활용 기반의 모델링은 품질의 확보가 어려움.
- 최적화된 형태 변환: 효과적인 Feature를 확보하는 것이 데이터 분석에서 가장 중요함.

### 차원 축소: 원본 데이터로부터 새로운 특징의 집합을 생성. 고차원 원시 데이터 셋을 저차원으로 축소.

- 범주 인코딩: 크게 Nominal(순서가 없는)과 Ordinal(순서가 있는)으로 나뉘는 범주형 변수. 숫자가 아닌 범주 변수 값을 숫자로 표현.
* One-hot Encoding: Nominal한 변수를 처리. K개의 범주를 지닌 범주형 변수를 K개의 변수로 변환.

### 결합 및 분해: 데이터 셋 변수들의 조합을 기반으로 새로운 특징을 구축. 변수간의 연산 혹은 분해를 통해 새로운 특징을 구축.
- 결합
1. Add/Divide: 종합적 수치 파악.
2. Subtract: 특정 수치의 편중 정도 파악.
3. Multiply: Interaction Feature로 시너지 효과 파악. 회귀 분석에 많이 사용함.

- 분해
1. Separate: 특정 변수 활용 기반의 새로운 의미를 파악할 수 있는 특징을 생성. 도메인 지식 및 일반적 개념 기반으로 생성 가능.

### 차원 축소: 원본 데이터로부터 새로운 특징의 집합을 생성. 고차원 원시 데이터 셋을 저차원으로 축소.
- PCA(Principal Compnent Analysis)
1. 변수들이 지닌 정보를 최대한 확보하는 저차원 데이터로 생성.
2. 서로 연관된 변수들이 관측되었을 때, 원본 데이터 분산 기반의 특징을 생성함. 
3. 주성분 간이 서로 독립을 이루도록함.

- Featurization via Clustering: 군집 분석 기반의 고차원 데이터를 하나의 특징으로 차원 축소. 
1. 이렇게 획득한 군집결과 특징을 분류/회귀 등 문제해결을 위한 입력변수로 활용(Stacking). 
2. 여러개의 특징을 하나의 특징으로 축소하여 모델 연산 비용 감소 추구.

- K-Means 알고리즘: 비슷한 특성을 가진 데이터들을 그룹으로 묶는 군집화 기법. 데이터가 원형으로 뭉쳐져 있는 경우에 잘 작동.
1. 초기 중심(Centroid) 무작위로 선택.
2. 각 데이터 포인트와 가까운 중심에 데이터 포인트 할당. 유클리드 거리가 주로 사용됨.
3. 데이터 포인트들의 평균을 계산하여 새로운 중심을 업데이트.
4. 2번과 3번을 데이터 포인터들이 변하지 않을 때까지 반복.
5. 데이터 포인터들이 변하지 않으면 알고리즘 종료.

## 12. 데이터 전처리 이해와 실무\_데이터 축소 - 특징 선택

### Feature Selection: 가장 좋은 성능을 보여줄 수 있는 데이터의 Subset(부분 집합)을 찾아내는 방법.
- 목적
1. 특징 생성과는 다르게 원 데이터 공간 내 유의미한 특징을 선택하는 기법.
2. 원본 데이터에서 가장 유용한 특징만을 선택.

### 특징 선택 종류
- Filter: 특징들에 대한 통계적 점수를 부여하여 순위를 매기고 선택하는 방법론. 실행 속도가 빠르다는 측면에서 시간 및 비용 측면의 장점을 보임.
1. Chi-square filter(카이제곱 필터): 범주형인 독립 및 종속 변수 간의 유의미성을 도출하기 위한 통계적 방안. 연속형 범주를 이산화하여 활용 가능. 과자를 좋아하는 학생들이 과학 실험을 좋아하는지 확인하는 것처럼, 범주형 변수 간의 관계를 확인.
2. Correlation filster: 연속적인 독립 및 종속변수 간 유의미성을 도출하기 위한 통계적 방안. 보통 threshold(임계치) 설정하여 변수 선택. 키와 몸무게처럼, 연속적인 변수 간의 관계를 확인.

- Wrapper: 특징들의 조합을 지도학습 기반 알고리즘에 반복적으로 적용하여 특징을 선택하는 방법론. 최적의 데이터 조합을 찾기 때문에 성능 관점상 유용하나 시간과 비용이 크게 발생.
1. 반복적 특징 조합 탐색: 원본 데이터셋 변수들의 다양한 조합을 모델에 적용. 최적의 subset을 도출하는 방법론. Recursive Feature Elemination이 대표적인 방식. 가장 좋은 옷 조합을 찾기 위해 옷장의 옷을 계속 바꿔보는 것처럼, 최적의 특징 조합을 찾음.

- Embedded: 모델 정확도에 기여하는 특징들을 선택하는 방법론. Filter와 Wrapper의 장점을 결합. 모델의 학습 및 생성과정에서 최적의 특징을 선택하는 방법.
1. 알고리즘 내 자체 내장 함수로 특징을 선택. 학습과정에서 최적화된 변수를 선택. 트리 계열 모델 기반의 특징 선택이 대표적.

### 특징 선택 알고리즘
- Boruta Algorithm: 기존 데이터를 임의로 복제하여 랜덤 변수(shadow)를 생성하고 원 자료와 결합하여 랜덤포레스트 모형에 적용함. shoadow 보다 중요도가 낮을 경우 중요하지 않은 변수로 판단 후 제거함. 친구들과 숨바꼭질을 할 때, 진짜 친구와 가짜 친구(인형)를 섞어 놓고, 진짜 친구를 찾는 것처럼 중요한 변수를 찾음.

## 13. 데이터 탐색 이해와 실무\_일변량 비시각화 탐색

- 대상: 하나의 변수
- 방법: 시각화를 사용하지 않는 통계적 방법
- 예: 평균, 중앙값, 표준편차, 왜도, 첨도 등의 통계치 계산
- 목적: 해당 변수의 분포, 중심 경향, 변동성 등의 기본 통계적 특성 파악

## 14. 데이터 탐색 이해와 실무\_일변량 시각화 탐색

- 대상: 하나의 변수
- 방법: 시각화 방법 사용
- 예: 히스토그램, 박스 플롯, 도수 분포표 등
- 목적: 데이터의 분포나 이상치 등을 직관적으로 파악

## 15. 데이터 탐색 이해와 실무\_다변량 비시각화 탐색

- 대상: 두 개 이상의 변수
- 방법: 시각화를 사용하지 않는 통계적 방법
- 예: 상관 계수, 공분산, 두 변수의 평균 차이 검정 등
- 목적: 변수 간의 관계나 연관성 파악

## 16. 데이터 탐색 이해와 실무\_다변량 시각화 탐색

- 대상: 두 개 이상의 변수
- 방법: 시각화 방법 사용
- 예: 산점도, 히트맵, 버블 차트, 페어 플롯 등
- 목적: 변수 간의 관계나 패턴, 그룹 내의 차이를 직관적으로 파악

## 17. 데이터 분석 이해와 실무\_가설의 의의와 검정

## 18. 데이터 분석 이해와 실무\_상관 분석

## 19. 데이터 분석 이해와 실무\_회귀 분석

## 20. 데이터 분석 이해와 실무\_시계열 분석

## 21. 데이터 시각화 이해와 실무\_정적 시각화 개요

## 22. 데이터 시각화 이해와 실무\_정적 시각화 실습 - matplotlib 활용

## 23. 데이터 시각화 이해와 실무\_정적 시각화 실습 - seaborn 활용

## 24. 데이터 시각화 이해와 실무\_동적 시각화 개요

## 25. 데이터 시각화 이해와 실무\_동적 시각화 실습 - plotly 활용

## 26. 데이터 시각화 이해와 실무\_UI 시각화 실습 - streamlit 활용
