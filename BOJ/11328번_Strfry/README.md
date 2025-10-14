# 11328번: Strfry - <img src="https://static.solved.ac/tier_small/4.svg" style="height:20px" /> Bronze II

<!-- performance -->

<!-- 문제 제출 후 깃허브에 푸시를 했을 때 제출한 코드의 성능이 입력될 공간입니다.-->

<!-- end -->

## 문제

[문제 링크](https://boj.kr/11328)

<p>C 언어 프로그래밍에서 문자열(string)은 native한 자료형이 아니다. 사실, 문자열은 그저, 문자열의 끝을 표시하기 위한 말단의 NULL이 사용된, 문자들로 이루어진 문자열일 뿐이다. 하지만 프로그래밍 언어에서 문자열을 다루는 것은 매우 중요하기 때문에, C 표준 라이브러리는 문자열을 다루는 데에 매우 유용한 함수들을 제공하고 있다 : 그들 중에는&nbsp;<strong>strcpy</strong>,&nbsp;<strong>strcmp</strong>,&nbsp;<strong>strtol</strong>,&nbsp;<strong>strtok</strong>,&nbsp;<strong>strlen</strong>, <strong>strcat</strong>&nbsp;가 있다.</p>

<p>하지만, 잘 알려져 있지 않으며, 잘 사용되지도 않는 함수가 하나 있다 :&nbsp;<strong>strfry</strong>&nbsp;함수다.&nbsp;<strong>strfry</strong>&nbsp;함수는 입력된 문자열을 무작위로 재배열하여 새로운 문자열을 만들어낸다. (역자 주 : 여기에서 입력된 문자열과 새로 재배열된 문자열이 다를 필요는 없다.)</p>

<p>두 개의 문자열에 대해, 2번째 문자열이 1번째 문자열에&nbsp;<strong>strfry</strong>&nbsp;함수를 적용하여 얻어질 수 있는지 판단하라.</p>

## 입력

<p>입력의 첫 번째 줄은 테스트 케이스의 수&nbsp;0 &lt;&nbsp;<strong>N</strong>&nbsp;&lt; 1001 이다.</p>

<p>각각의 테스트 케이스는 하나의 줄에 영어 소문자들로만 이루어진 두 개의 문자열이 한 개의 공백으로 구분되어 주어진다. 각각의 문자열의 길이는 최대 1000 이다.</p>

## 출력

<p>각각의 테스트 케이스에 대해,&nbsp;2번째 문자열이 1번째 문자열에&nbsp;<strong>strfry</strong>&nbsp;함수를 적용하여 얻어질 수 있는지의 여부를 "Impossible"(불가능) 또는 "Possible"(가능)으로 나타내시오. (따옴표는 제외하고 출력한다.)</p>

## 소스코드

[소스코드 보기](Strfry.py)