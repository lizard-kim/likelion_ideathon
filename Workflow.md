# Workflow for Collaboration

협업 전략은 [`Gihub-flow`](https://ujuc.github.io/2015/12/16/git-flow-github-flow-gitlab-flow/)입니다!

## 시작하기

```
git clone https://github.com/lizard-kim/likelion_ideathon.git
cd likelion_ideathon
git status # 현재 상태를 출력합니다.
```

## 기능별/작업별 이슈 열기

레포지토리의 Issues탭 에서 `New Issue`를 눌러 새로운이슈를 생성합니다. 이때 본문에는 구체적으로 어떠한 작업인지를 명시하고 오른쪽 collection에서 새로운 이슈가 어떠한 종류에 속하는 지 (Dev-major / Dev-minor / Data & Posting 등), 누구에게 배정되었는 지 등의 정보를 입력합니다.

## feature 브랜치 만들기

클론한 로컬 레포지토리에서 `이슈번호-기능설명`의 형태로 브랜치를 만들고 해당 브랜치로 이동합니다. 이슈번호는 이슈제목 옆에 `#이슈번호`의 형태로 확인할 수 있습니다. 이때 `master`브랜치에서 새로운 브랜치로 이동하게 되는데 `master`브랜치는 *관리*를 위한 브랜치이지 *작업*을 위한 브랜치가 아님을 명심합니다. *master 브랜치에서는 직접적으로 코드를 수정하지 않습니다.*

```
# 예시
git checkout -b 1-init # checkout은 원래 다른 브랜치로 이동할 때 쓰는 명령어, -b 옵션을 붙이면 새로운 브랜치를 만들면서 이동한다.
git status # 작업 브랜치의 이름이 출력되는 지 확인합니다.
git push --set-upstream origin 1-init # 깃헙의 원격 레포지토리에 방금 만든 브랜치를 푸시합니다.
```

작업 브랜치로 이동한 후 코드를 수정합니다.

## 작업 관리하기; 커밋하고 feature 브랜치 origin에 푸시하기

작업 하는 도중에 `commit` 을 통해 코드의 버전을 관리할 수 있습니다. 이때 커밋 메세지에 `[#이슈번호]`를 붙이면 깃헙의 이슈 트래커에서 해당 이슈와 관련된 커밋을 모아서 볼 수 있습니다.

```
# 예시
git commit -m  "[#1] Add Materialize Assets" # -m 옵션은 한줄 짜리 커밋 메세지를 작성할 때 사용합니다.
git log # 커밋 이력을 확인할 수 있습니다.
git push # orgin의 동일 브랜치로 작업내용을 푸시합니다.
```

Github-flow에서는 수시로 작업내용을 깃헙의 레포지토리로 푸시할 것을 권장합니다. 그래야 팀원들이 서로의 작업내용을 이해하고 예상치 않은 작업내용의 소실을 방지할 수 있기 때문입니다.

## 출시하기; 풀 리퀘스트 생성하기

마지막 작업 내용까지 커밋과 푸시를 완료했다면 깃헙 레포지토리의 `Pull request`탭에서 자신이 작업한 `feature 브랜치`를 `master 브랜치`로 당기는 pull request를 생성합니다. 요청이 정상적으로 생성되면 팀원들이게 알리고 리뷰를 받습니다. 팀원들이 `merge`에 동의하고 아무런 conflict도 발견되지 않는다면 merge 버튼을 눌러 작업내용을 `master 브랜치`에 반영합니다. 병합이 정상적으로 완료되면 로컬에서도 master 브랜치로 옮겨가 최신 코드를 받습니다.

```
# 예시
git checkout master # 작업완료한 브랜치에서 로컬의 master bracnh로 옮겨갑니다.
git pull # 최신화된 코드를 받고 다음 작업을 준비합니다.
# git branch -d 1-init 처럼 로컬에서 작업 완료한 브랜치를 지울 수도 있습니다.
```

그리고 이슈 탭에서 `close issue` 버튼을 이용해 작업이 완료된 `issue`를 `close` 상태로 전환합니다.

## 주의점

- 새로운 기능 브랜치를 만들고 작업을 시작할 때에는 시작 직전에 `pull request`로 최신화된 `master 브랜치`에서 분기해야 충돌을 최소화 할 수 있습니다.