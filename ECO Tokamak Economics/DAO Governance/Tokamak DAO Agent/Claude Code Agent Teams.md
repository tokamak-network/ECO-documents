Agent Teams는 하나의 Claude Code 세션이 모든 걸 순차적으로 처리하던 방식에서, 리드 에이전트가 작업을 분할하고 여러 팀메이트가 병렬로 작업하는 방식으로 바뀐 것이다. 각 팀메이트는 독립된 컨텍스트 윈도우를 가지고 서로 직접 소통하며 공유 태스크 리스트를 통해 조율한다.

## ./claude/.settings

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

팀을 만들 때는 각 팀메이트의 역할을 구체적으로 지정하는 것이 핵심이다.

I'm designing a CLI tool that helps developers track TODO comments across their codebase. Create an agent team to explore this from different angles: one teammate on UX, one on technical architecture, and one playing devil's advocate.

### 조작법

- 팀메이트 전환: `Shift + Up/Down`으로 직접 대화 가능
- Delegate 모드: `Shift + Tab` —> 리드가 직접 작업하지 않고 조율만 하게 강제
- Split-pane 모드: tmux나 iTerm2에서 각 팀메이트를 별도 패널로 확인 가능하다.