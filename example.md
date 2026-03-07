# Test framework and tests used in project

**Session ID:** ses_3be52f48bffeKNtDwOJJ8J7GUO
**Created:** 2026/2/9 17:13:05
**Updated:** 2026/2/9 20:07:01

---

## User

I can see that there are many scripts and configuration files in the .github directory, which represent some test actions executed by this project. Please help me analyze these files in detail, clarify the relationships between these scripts and configuration files, examine the specific testing content, and provide me with a clear architectural diagram or similar formats

---

## Assistant (Build · openrouter/pony-alpha · 16.1s)

_Thinking:_

The user wants me to analyze the GitHub Actions workflows and related scripts in the .github directory to understand the testing architecture of this PyTorch project. Let me explore the .github directory structure and read the relevant files.

**Tool: bash**

**Input:**
```json
{
  "command": "ls -la .github",
  "description": "List .github directory contents",
  "workdir": "D:\\oss\\opensource\\pytorch-2.6.0"
}
```

**Output:**
```
total 110
drwxr-xr-x 1 liutuo 197121     0 Nov 13 16:48 .
drwxr-xr-x 1 liutuo 197121     0 Nov 13 16:54 ..
drwxr-xr-x 1 liutuo 197121     0 Nov 13 16:48 ISSUE_TEMPLATE
-rw-r--r-- 1 liutuo 197121    20 Jan 29  2025 PULL_REQUEST_TEMPLATE.md
-rw-r--r-- 1 liutuo 197121  1820 Jan 29  2025 actionlint.yaml
drwxr-xr-x 1 liutuo 197121     0 Nov 13 16:48 actions
-rw-r--r-- 1 liutuo 197121   548 Jan 29  2025 auto_request_review.yml
drwxr-xr-x 1 liutuo 197121     0 Nov 13 16:48 ci_commit_pins
-rw-r--r-- 1 liutuo 197121  1098 Jan 29  2025 label_to_label.yml
-rw-r--r-- 1 liutuo 197121  2782 Jan 29  2025 labeler.yml
-rw-r--r-- 1 liutuo 197121 10906 Jan 29  2025 merge_rules.yaml
-rw-r--r-- 1 liutuo 197121   611 Jan 29  2025 nitpicks.yml
-rw-r--r-- 1 liutuo 197121   550 Jan 29  2025 pytorch-circleci-labels.yml
-rw-r--r-- 1 liutuo 197121   718 Jan 29  2025 pytorch-probot.yml
-rwxr-xr-x 1 liutuo 197121   134 Jan 29  2025 regenerate.sh
drwxr-xr-x 1 liutuo 197121     0 Nov 13 16:48 requirements
-rw-r--r-- 1 liutuo 197121   352 Jan 29  2025 requirements-gha-cache.txt
drwxr-xr-x 1 liutuo 197121     0 Nov 13 16:48 scripts
drwxr-xr-x 1 liutuo 197121     0 Nov 13 16:48 templates
drwxr-xr-x 1 liutuo 197121     0 Nov 13 16:48 workflows

```

**Tool: glob**

**Input:**
```json
{
  "path": "D:\\oss\\opensource\\pytorch-2.6.0\\.github",
  "pattern": "**/*.yml"
}
```

**Output:**
```
D:\oss\opensource\pytorch-2.6.0\.github\label_to_label.yml
D:\oss\opensource\pytorch-2.6.0\.github\labeler.yml
D:\oss\opensource\pytorch-2.6.0\.github\pytorch-probot.yml
D:\oss\opensource\pytorch-2.6.0\.github\pytorch-circleci-labels.yml
D:\oss\opensource\pytorch-2.6.0\.github\nitpicks.yml
D:\oss\opensource\pytorch-2.6.0\.github\ISSUE_TEMPLATE\pt2-bug-report.yml
D:\oss\opensource\pytorch-2.6.0\.github\ISSUE_TEMPLATE\feature-request.yml
D:\oss\opensource\pytorch-2.6.0\.github\ISSUE_TEMPLATE\documentation.yml
D:\oss\opensource\pytorch-2.6.0\.github\ISSUE_TEMPLATE\config.yml
D:\oss\opensource\pytorch-2.6.0\.github\ISSUE_TEMPLATE\bug-report.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_xpu-test.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_win-test.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_win-build.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_runner-determinator.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_rocm-test.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_mac-test.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_mac-test-mps.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_mac-build.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_linux-test.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_linux-build.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_docs.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_binary-upload.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_binary-test-linux.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_binary-build-linux.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\_bazel-build-test.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\xpu.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\weekly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\upload_test_stats_intermediate.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\upload-torch-dynamo-perf-stats.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\upload-test-stats.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\upload-test-stats-while-running.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\update_pytorch_labels.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\update-viablestrict.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\unstable.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\unstable-periodic.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\tryrebase.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\trymerge.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\trunk.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\torchbench.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\target_determination.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\target-determination-indexer.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\stale.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\slow.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\scorecards.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\s390.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\runner-determinator-validator.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\rocm.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\revert.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\pull.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\periodic.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\nitpicker.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\nightly-s3-uploads.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\mac-mps.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\llm_td_retrieval.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\linux-aarch64.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\lint.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\lint-bc.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\lint-autoformat.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\inductor.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\inductor-unittest.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\inductor-rocm.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\inductor-periodic.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\inductor-perf-test-nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\inductor-perf-test-nightly-x86.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\inductor-perf-test-nightly-macos.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\inductor-perf-test-nightly-aarch64.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\inductor-perf-compare.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\inductor-micro-benchmark.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\inductor-micro-benchmark-x86.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-windows-binary-wheel-nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-windows-binary-libtorch-release-nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-windows-binary-libtorch-release-main.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-windows-binary-libtorch-debug-nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-windows-binary-libtorch-debug-main.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-macos-arm64-binary-wheel-nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-macos-arm64-binary-libtorch-cxx11-abi-nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-linux-s390x-binary-manywheel-nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-linux-binary-manywheel-nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-linux-binary-manywheel-main.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-linux-binary-libtorch-pre-cxx11-nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-linux-binary-libtorch-pre-cxx11-main.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-linux-binary-libtorch-cxx11-abi-nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-linux-binary-libtorch-cxx11-abi-main.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\generated-linux-aarch64-binary-manywheel-nightly.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\docker-release.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\docker-builds.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\docathon-sync-label.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\delete_old_branches.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\create_release.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\close-nonexistent-disable-issues.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\cherry-pick.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\check_mergeability_ghstack.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\check-labels.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\build-triton-wheel.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\build-manywheel-images.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\build-manywheel-images-s390x.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\build-magma-windows.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\build-magma-linux.yml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\build-libtorch-images.yml

(Results are truncated. Consider using a more specific path or pattern.)
```

**Tool: glob**

**Input:**
```json
{
  "path": "D:\\oss\\opensource\\pytorch-2.6.0\\.github",
  "pattern": "**/*.yaml"
}
```

**Output:**
```
D:\oss\opensource\pytorch-2.6.0\.github\actionlint.yaml
D:\oss\opensource\pytorch-2.6.0\.github\workflows\runner_determinator_script_sync.yaml
D:\oss\opensource\pytorch-2.6.0\.github\merge_rules.yaml
```

---

## Assistant (Build · openrouter/pony-alpha · 16.1s)

_Thinking:_

Let me explore the workflows directory more thoroughly and the scripts directory to understand the architecture better.

**Tool: bash**

**Input:**
```json
{
  "command": "ls -la .github/workflows | head -100",
  "description": "List all workflow files",
  "workdir": "D:\\oss\\opensource\\pytorch-2.6.0"
}
```

**Output:**
```
total 1388
drwxr-xr-x 1 liutuo 197121      0 Nov 13 16:48 .
drwxr-xr-x 1 liutuo 197121      0 Nov 13 16:48 ..
-rw-r--r-- 1 liutuo 197121   7797 Jan 29  2025 _bazel-build-test.yml
-rw-r--r-- 1 liutuo 197121  11161 Jan 29  2025 _binary-build-linux.yml
-rw-r--r-- 1 liutuo 197121   8443 Jan 29  2025 _binary-test-linux.yml
-rw-r--r-- 1 liutuo 197121   6641 Jan 29  2025 _binary-upload.yml
-rw-r--r-- 1 liutuo 197121   9103 Jan 29  2025 _docs.yml
-rw-r--r-- 1 liutuo 197121  13748 Jan 29  2025 _linux-build.yml
-rw-r--r-- 1 liutuo 197121  20701 Jan 29  2025 _linux-test.yml
-rw-r--r-- 1 liutuo 197121   8574 Jan 29  2025 _mac-build.yml
-rw-r--r-- 1 liutuo 197121   6394 Jan 29  2025 _mac-test-mps.yml
-rw-r--r-- 1 liutuo 197121   8960 Jan 29  2025 _mac-test.yml
-rw-r--r-- 1 liutuo 197121  11202 Jan 29  2025 _rocm-test.yml
-rw-r--r-- 1 liutuo 197121  29030 Jan 29  2025 _runner-determinator.yml
-rw-r--r-- 1 liutuo 197121   7176 Jan 29  2025 _win-build.yml
-rw-r--r-- 1 liutuo 197121  10149 Jan 29  2025 _win-test.yml
-rw-r--r-- 1 liutuo 197121  11395 Jan 29  2025 _xpu-test.yml
-rw-r--r-- 1 liutuo 197121   2476 Jan 29  2025 assigntome-docathon.yml
-rw-r--r-- 1 liutuo 197121    802 Jan 29  2025 auto_request_review.yml
-rw-r--r-- 1 liutuo 197121   2640 Jan 29  2025 build-almalinux-images.yml
-rw-r--r-- 1 liutuo 197121   6075 Jan 29  2025 build-libtorch-images.yml
-rw-r--r-- 1 liutuo 197121   2143 Jan 29  2025 build-magma-linux.yml
-rw-r--r-- 1 liutuo 197121   2491 Jan 29  2025 build-magma-windows.yml
-rw-r--r-- 1 liutuo 197121   1997 Jan 29  2025 build-manywheel-images-s390x.yml
-rw-r--r-- 1 liutuo 197121  17348 Jan 29  2025 build-manywheel-images.yml
-rw-r--r-- 1 liutuo 197121   9117 Jan 29  2025 build-triton-wheel.yml
-rw-r--r-- 1 liutuo 197121   2106 Jan 29  2025 check-labels.yml
-rw-r--r-- 1 liutuo 197121   2573 Jan 29  2025 check_mergeability_ghstack.yml
-rw-r--r-- 1 liutuo 197121   1786 Jan 29  2025 cherry-pick.yml
-rw-r--r-- 1 liutuo 197121    965 Jan 29  2025 close-nonexistent-disable-issues.yml
-rw-r--r-- 1 liutuo 197121   4565 Jan 29  2025 create_release.yml
-rw-r--r-- 1 liutuo 197121    797 Jan 29  2025 delete_old_branches.yml
-rw-r--r-- 1 liutuo 197121    828 Jan 29  2025 docathon-sync-label.yml
-rw-r--r-- 1 liutuo 197121   5740 Jan 29  2025 docker-builds.yml
-rw-r--r-- 1 liutuo 197121   6777 Jan 29  2025 docker-release.yml
-rw-r--r-- 1 liutuo 197121  38023 Jan 29  2025 generated-linux-aarch64-binary-manywheel-nightly.yml
-rw-r--r-- 1 liutuo 197121   3263 Jan 29  2025 generated-linux-binary-libtorch-cxx11-abi-main.yml
-rw-r--r-- 1 liutuo 197121  20749 Jan 29  2025 generated-linux-binary-libtorch-cxx11-abi-nightly.yml
-rw-r--r-- 1 liutuo 197121   3253 Jan 29  2025 generated-linux-binary-libtorch-pre-cxx11-main.yml
-rw-r--r-- 1 liutuo 197121  13099 Jan 29  2025 generated-linux-binary-libtorch-pre-cxx11-nightly.yml
-rw-r--r-- 1 liutuo 197121  10233 Jan 29  2025 generated-linux-binary-manywheel-main.yml
-rw-r--r-- 1 liutuo 197121 169720 Jan 29  2025 generated-linux-binary-manywheel-nightly.yml
-rw-r--r-- 1 liutuo 197121  20830 Jan 29  2025 generated-linux-s390x-binary-manywheel-nightly.yml
-rw-r--r-- 1 liutuo 197121   6245 Jan 29  2025 generated-macos-arm64-binary-libtorch-cxx11-abi-nightly.yml
-rw-r--r-- 1 liutuo 197121  30094 Jan 29  2025 generated-macos-arm64-binary-wheel-nightly.yml
-rw-r--r-- 1 liutuo 197121  11847 Jan 29  2025 generated-windows-binary-libtorch-debug-main.yml
-rw-r--r-- 1 liutuo 197121  48444 Jan 29  2025 generated-windows-binary-libtorch-debug-nightly.yml
-rw-r--r-- 1 liutuo 197121  11867 Jan 29  2025 generated-windows-binary-libtorch-release-main.yml
-rw-r--r-- 1 liutuo 197121  48538 Jan 29  2025 generated-windows-binary-libtorch-release-nightly.yml
-rw-r--r-- 1 liutuo 197121 298885 Jan 29  2025 generated-windows-binary-wheel-nightly.yml
-rw-r--r-- 1 liutuo 197121   1653 Jan 29  2025 inductor-micro-benchmark-x86.yml
-rw-r--r-- 1 liutuo 197121   2922 Jan 29  2025 inductor-micro-benchmark.yml
-rw-r--r-- 1 liutuo 197121   3114 Jan 29  2025 inductor-perf-compare.yml
-rw-r--r-- 1 liutuo 197121   8647 Jan 29  2025 inductor-perf-test-nightly-aarch64.yml
-rw-r--r-- 1 liutuo 197121   1900 Jan 29  2025 inductor-perf-test-nightly-macos.yml
-rw-r--r-- 1 liutuo 197121   5602 Jan 29  2025 inductor-perf-test-nightly-x86.yml
-rw-r--r-- 1 liutuo 197121   7272 Jan 29  2025 inductor-perf-test-nightly.yml
-rw-r--r-- 1 liutuo 197121  16090 Jan 29  2025 inductor-periodic.yml
-rw-r--r-- 1 liutuo 197121   3346 Jan 29  2025 inductor-rocm.yml
-rw-r--r-- 1 liutuo 197121   8155 Jan 29  2025 inductor-unittest.yml
-rw-r--r-- 1 liutuo 197121   4784 Jan 29  2025 inductor.yml
-rw-r--r-- 1 liutuo 197121   1641 Jan 29  2025 lint-autoformat.yml
-rw-r--r-- 1 liutuo 197121   1091 Jan 29  2025 lint-bc.yml
-rw-r--r-- 1 liutuo 197121  11676 Jan 29  2025 lint.yml
-rw-r--r-- 1 liutuo 197121   2294 Jan 29  2025 linux-aarch64.yml
-rw-r--r-- 1 liutuo 197121   3895 Jan 29  2025 llm_td_retrieval.yml
-rw-r--r-- 1 liutuo 197121   1559 Jan 29  2025 mac-mps.yml
-rw-r--r-- 1 liutuo 197121   1751 Jan 29  2025 nightly-s3-uploads.yml
-rw-r--r-- 1 liutuo 197121   3618 Jan 29  2025 nightly.yml
-rw-r--r-- 1 liutuo 197121    836 Jan 29  2025 nitpicker.yml
-rw-r--r-- 1 liutuo 197121  17892 Jan 29  2025 periodic.yml
-rw-r--r-- 1 liutuo 197121  29539 Jan 29  2025 pull.yml
-rw-r--r-- 1 liutuo 197121   2231 Jan 29  2025 revert.yml
-rw-r--r-- 1 liutuo 197121   2182 Jan 29  2025 rocm.yml
-rw-r--r-- 1 liutuo 197121   1816 Jan 29  2025 runner-determinator-validator.yml
-rw-r--r-- 1 liutuo 197121   1500 Jan 29  2025 runner_determinator_script_sync.yaml
-rw-r--r-- 1 liutuo 197121    765 Jan 29  2025 s390.yml
-rw-r--r-- 1 liutuo 197121   1705 Jan 29  2025 scorecards.yml
-rw-r--r-- 1 liutuo 197121   6338 Jan 29  2025 slow.yml
-rw-r--r-- 1 liutuo 197121   6295 Jan 29  2025 stale.yml
-rw-r--r-- 1 liutuo 197121   5504 Jan 29  2025 target-determination-indexer.yml
-rw-r--r-- 1 liutuo 197121   3257 Jan 29  2025 target_determination.yml
-rw-r--r-- 1 liutuo 197121   2587 Jan 29  2025 torchbench.yml
-rw-r--r-- 1 liutuo 197121  11431 Jan 29  2025 trunk.yml
-rw-r--r-- 1 liutuo 197121   4127 Jan 29  2025 trymerge.yml
-rw-r--r-- 1 liutuo 197121   1671 Jan 29  2025 tryrebase.yml
-rw-r--r-- 1 liutuo 197121   1481 Jan 29  2025 unstable-periodic.yml
-rw-r--r-- 1 liutuo 197121   1302 Jan 29  2025 unstable.yml
-rw-r--r-- 1 liutuo 197121   1954 Jan 29  2025 update-viablestrict.yml
-rw-r--r-- 1 liutuo 197121    907 Jan 29  2025 update_pytorch_labels.yml
-rw-r--r-- 1 liutuo 197121   1051 Jan 29  2025 upload-test-stats-while-running.yml
-rw-r--r-- 1 liutuo 197121   5654 Jan 29  2025 upload-test-stats.yml
-rw-r--r-- 1 liutuo 197121   3339 Jan 29  2025 upload-torch-dynamo-perf-stats.yml
-rw-r--r-- 1 liutuo 197121   1245 Jan 29  2025 upload_test_stats_intermediate.yml
-rw-r--r-- 1 liutuo 197121   2562 Jan 29  2025 weekly.yml
-rw-r--r-- 1 liutuo 197121   3415 Jan 29  2025 xpu.yml

```

**Tool: bash**

**Input:**
```json
{
  "command": "ls -la .github/scripts",
  "description": "List scripts directory",
  "workdir": "D:\\oss\\opensource\\pytorch-2.6.0"
}
```

**Output:**
```
total 1397
drwxr-xr-x 1 liutuo 197121      0 Nov 13 16:48 .
drwxr-xr-x 1 liutuo 197121      0 Nov 13 16:48 ..
-rw-r--r-- 1 liutuo 197121   3042 Jan 29  2025 README.md
drwxr-xr-x 1 liutuo 197121      0 Nov 13 16:48 amd
-rwxr-xr-x 1 liutuo 197121   6579 Jan 29  2025 build_triton_wheel.py
-rwxr-xr-x 1 liutuo 197121   1958 Jan 29  2025 check_labels.py
-rwxr-xr-x 1 liutuo 197121   9357 Jan 29  2025 cherry_pick.py
-rw-r--r-- 1 liutuo 197121   5415 Jan 29  2025 close_nonexistent_disable_issues.py
-rwxr-xr-x 1 liutuo 197121   2527 Jan 29  2025 collect_ciflow_labels.py
-rw-r--r-- 1 liutuo 197121   1249 Jan 29  2025 comment_on_pr.py
-rw-r--r-- 1 liutuo 197121   1772 Jan 29  2025 convert_lintrunner_annotations_to_github.py
-rw-r--r-- 1 liutuo 197121  10484 Jan 29  2025 delete_old_branches.py
-rw-r--r-- 1 liutuo 197121   1643 Jan 29  2025 docathon-label-sync.py
-rw-r--r-- 1 liutuo 197121   9128 Jan 29  2025 drci_mocks.json.gz
-rwxr-xr-x 1 liutuo 197121   2525 Jan 29  2025 ensure_actions_will_cancel.py
-rwxr-xr-x 1 liutuo 197121   1113 Jan 29  2025 export_pytorch_labels.py
-rw-r--r-- 1 liutuo 197121   2925 Jan 29  2025 file_io_utils.py
-rwxr-xr-x 1 liutuo 197121  22837 Jan 29  2025 filter_test_configs.py
-rwxr-xr-x 1 liutuo 197121  19068 Jan 29  2025 generate_binary_build_matrix.py
-rwxr-xr-x 1 liutuo 197121  13773 Jan 29  2025 generate_ci_workflows.py
-rwxr-xr-x 1 liutuo 197121   1548 Jan 29  2025 generate_docker_release_matrix.py
-rwxr-xr-x 1 liutuo 197121   3602 Jan 29  2025 generate_pytorch_version.py
-rwxr-xr-x 1 liutuo 197121    405 Jan 29  2025 get_aws_session_tokens.py
-rw-r--r-- 1 liutuo 197121   5601 Jan 29  2025 get_workflow_job_id.py
-rw-r--r-- 1 liutuo 197121   7225 Jan 29  2025 github_utils.py
-rwxr-xr-x 1 liutuo 197121  15944 Jan 29  2025 gitutils.py
-rw-r--r-- 1 liutuo 197121 680483 Jan 29  2025 gql_mocks.json.gz
-rw-r--r-- 1 liutuo 197121    261 Jan 29  2025 kill_active_ssh_sessions.ps1
-rw-r--r-- 1 liutuo 197121   4269 Jan 29  2025 label_utils.py
-rwxr-xr-x 1 liutuo 197121   2283 Jan 29  2025 lint_native_functions.py
-rwxr-xr-x 1 liutuo 197121   2245 Jan 29  2025 lintrunner.sh
-rwxr-xr-x 1 liutuo 197121    734 Jan 29  2025 parse_ref.py
-rwxr-xr-x 1 liutuo 197121   1752 Jan 29  2025 pr-sanity-check.sh
-rw-r--r-- 1 liutuo 197121   3288 Jan 29  2025 pytest_cache.py
-rw-r--r-- 1 liutuo 197121   9049 Jan 29  2025 pytest_caching_utils.py
-rwxr-xr-x 1 liutuo 197121    205 Jan 29  2025 report_git_status.sh
-rw-r--r-- 1 liutuo 197121 213144 Jan 29  2025 rockset_mocks.json.gz
-rw-r--r-- 1 liutuo 197121  20939 Jan 29  2025 runner_determinator.py
drwxr-xr-x 1 liutuo 197121      0 Nov 13 16:48 s390x-ci
-rwxr-xr-x 1 liutuo 197121    861 Jan 29  2025 stop_runner_service.sh
-rw-r--r-- 1 liutuo 197121   1812 Jan 29  2025 tag_docker_images_for_release.py
-rwxr-xr-x 1 liutuo 197121    374 Jan 29  2025 td_llm_indexer.sh
-rw-r--r-- 1 liutuo 197121   5189 Jan 29  2025 test_check_labels.py
-rwxr-xr-x 1 liutuo 197121  37862 Jan 29  2025 test_filter_test_configs.py
-rwxr-xr-x 1 liutuo 197121   3121 Jan 29  2025 test_gitutils.py
-rw-r--r-- 1 liutuo 197121   3360 Jan 29  2025 test_label_utils.py
-rw-r--r-- 1 liutuo 197121   3157 Jan 29  2025 test_pytest_caching_utils.py
-rw-r--r-- 1 liutuo 197121  13144 Jan 29  2025 test_runner_determinator.py
-rwxr-xr-x 1 liutuo 197121  41726 Jan 29  2025 test_trymerge.py
-rw-r--r-- 1 liutuo 197121   6631 Jan 29  2025 test_tryrebase.py
-rwxr-xr-x 1 liutuo 197121  83457 Jan 29  2025 trymerge.py
-rw-r--r-- 1 liutuo 197121   3260 Jan 29  2025 trymerge_explainer.py
-rwxr-xr-x 1 liutuo 197121   9006 Jan 29  2025 tryrebase.py
-rwxr-xr-x 1 liutuo 197121   1043 Jan 29  2025 update_runner_determinator.py
-rwxr-xr-x 1 liutuo 197121   1314 Jan 29  2025 upload_aws_ossci.sh
-rw-r--r-- 1 liutuo 197121    582 Jan 29  2025 wait_for_ssh_to_drain.ps1
drwxr-xr-x 1 liutuo 197121      0 Nov 13 16:48 windows

```

**Tool: bash**

**Input:**
```json
{
  "command": "ls -la .github/actions",
  "description": "List actions directory",
  "workdir": "D:\\oss\\opensource\\pytorch-2.6.0"
}
```

**Output:**
```
total 8
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 .
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 ..
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 build-android
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 checkout-pytorch
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 chown-workspace
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 diskspace-cleanup
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 download-build-artifacts
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 download-td-artifacts
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 filter-test-configs
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 get-workflow-job-id
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 linux-test
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 pytest-cache-download
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 pytest-cache-upload
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 setup-linux
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 setup-rocm
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 setup-win
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 setup-xpu
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 teardown-rocm
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 teardown-win
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 teardown-xpu
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 test-pytorch-binary
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 upload-sccache-stats
drwxr-xr-x 1 liutuo 197121 0 Nov 13 16:48 upload-test-artifacts

```

---

## Assistant (Build · openrouter/pony-alpha · 20.5s)

_Thinking:_

.
Now let me read some key workflow files to understand the architecture better. I'll start with the main entry point workflows and then look at the reusable workflows (prefixed with _).
Now let me read some key workflow files to understand the architecture better. I'll start with the main entry point workflows and then look at the reusable workflows (prefixed with _).
Now let me read some key workflow files to understand the architecture better. I'll start with the main entry point workflows and then look at the reusable workflows (prefixed with _).

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\scripts\\README.md"
}
```

**Output:**
```
<file>
00001| # pytorch/.github
00002| 
00003| > NOTE: This README contains information for the `.github` directory but cannot be located there because it will overwrite the
00004| repo README.
00005| 
00006| This directory contains workflows and scripts to support our CI infrastructure that runs on GitHub Actions.
00007| 
00008| ## Workflows
00009| 
00010| - Pull CI (`pull.yml`) is run on PRs and on main.
00011| - Trunk CI (`trunk.yml`) is run on trunk to validate incoming commits. Trunk jobs are usually more expensive to run so we do not run them on PRs unless specified.
00012| - Scheduled CI (`periodic.yml`) is a subset of trunk CI that is run every few hours on main.
00013| - Binary CI is run to package binaries for distribution for all platforms.
00014| 
00015| ## Templates
00016| 
00017| Templates written in [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) are located in the `.github/templates` directory
00018| and used to generate workflow files for binary jobs found in the `.github/workflows/` directory. These are also a
00019| couple of utility templates used to discern common utilities that can be used amongst different templates.
00020| 
00021| ### (Re)Generating workflow files
00022| 
00023| You will need `jinja2` in order to regenerate the workflow files which can be installed using:
00024| ```bash
00025| pip install -r .github/requirements/regenerate-requirements.txt
00026| ```
00027| 
00028| Workflows can be generated / regenerated using the following command:
00029| ```bash
00030| .github/regenerate.sh
00031| ```
00032| 
00033| ### Adding a new generated binary workflow
00034| 
00035| New generated binary workflows can be added in the `.github/scripts/generate_ci_workflows.py` script. You can reference
00036| examples from that script in order to add the workflow to the stream that is relevant to what you particularly
00037| care about.
00038| 
00039| Different parameters can be used to achieve different goals, i.e. running jobs on a cron, running only on trunk, etc.
00040| 
00041| #### ciflow (trunk)
00042| 
00043| The label `ciflow/trunk` can be used to run `trunk` only workflows. This is especially useful if trying to re-land a PR that was
00044| reverted for failing a `non-default` workflow.
00045| 
00046| ## Infra
00047| 
00048| Currently most of our self hosted runners are hosted on AWS, for a comprehensive list of available runner types you
00049| can reference `.github/scale-config.yml`.
00050| 
00051| Exceptions to AWS for self hosted:
00052| * ROCM runners
00053| 
00054| ### Adding new runner types
00055| 
00056| New runner types can be added by committing changes to `.github/scale-config.yml`. Example: https://github.com/pytorch/pytorch/pull/70474
00057| 
00058| > NOTE: New runner types can only be used once the changes to `.github/scale-config.yml` have made their way into the default branch
00059| 
00060| ### Testing [pytorch/builder](https://github.com/pytorch/builder) changes
00061| 
00062| In order to test changes to the builder scripts:
00063| 
00064| 1. Specify your builder PR's branch and repo as `builder_repo` and  `builder_branch` in [`.github/templates/common.yml.j2`](https://github.com/pytorch/pytorch/blob/32356aaee6a77e0ae424435a7e9da3d99e7a4ca5/.github/templates/common.yml.j2#LL10C26-L10C32).
00065| 2. Regenerate workflow files with `.github/regenerate.sh` (see above).
00066| 3. Submit fake PR to PyTorch. If changing binaries build, add an appropriate label like `ciflow/binaries` to trigger the builds.
00067| 

(End of file - total 67 lines)
</file>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\pull.yml"
}
```

**Output:**
```
<file>
00001| name: pull
00002| 
00003| on:
00004|   pull_request:
00005|     branches-ignore:
00006|       - nightly
00007|   push:
00008|     branches:
00009|       - main
00010|       - release/*
00011|       - landchecks/*
00012|   workflow_dispatch:
00013|   schedule:
00014|     - cron: 29 8 * * *  # about 1:29am PDT
00015| 
00016| concurrency:
00017|   group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.sha }}-${{ github.event_name == 'workflow_dispatch' }}-${{ github.event_name == 'schedule' }}
00018|   cancel-in-progress: true
00019| 
00020| permissions: read-all
00021| 
00022| jobs:
00023|   llm-td:
00024|     if: github.repository_owner == 'pytorch'
00025|     name: before-test
00026|     uses: ./.github/workflows/llm_td_retrieval.yml
00027|     permissions:
00028|       id-token: write
00029|       contents: read
00030| 
00031|   target-determination:
00032|     name: before-test
00033|     uses: ./.github/workflows/target_determination.yml
00034|     needs: llm-td
00035|     permissions:
00036|       id-token: write
00037|       contents: read
00038| 
00039|   get-label-type:
00040|     name: get-label-type
00041|     uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
00042|     if: ${{ (github.event_name != 'schedule' || github.repository == 'pytorch/pytorch') && github.repository_owner == 'pytorch' }}
00043|     with:
00044|       triggering_actor: ${{ github.triggering_actor }}
00045|       issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
00046|       curr_branch: ${{ github.head_ref || github.ref_name }}
00047| 
00048|   linux-jammy-py3_9-gcc11-build:
00049|     name: linux-jammy-py3.9-gcc11
00050|     uses: ./.github/workflows/_linux-build.yml
00051|     needs: get-label-type
00052|     with:
00053|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00054|       build-environment: linux-jammy-py3.9-gcc11
00055|       docker-image-name: pytorch-linux-jammy-py3.9-gcc11
00056|       test-matrix: |
00057|         { include: [
00058|           { config: "default", shard: 1, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00059|           { config: "default", shard: 2, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00060|           { config: "default", shard: 3, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00061|           { config: "default", shard: 4, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00062|           { config: "default", shard: 5, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00063|           { config: "docs_test", shard: 1, num_shards: 1,  runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00064|           { config: "jit_legacy", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00065|           { config: "backwards_compat", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00066|           { config: "distributed", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00067|           { config: "distributed", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00068|           { config: "numpy_2_x", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00069|         ]}
00070|     secrets: inherit
00071| 
00072|   linux-jammy-py3_9-gcc11-test:
00073|     name: linux-jammy-py3.9-gcc11
00074|     uses: ./.github/workflows/_linux-test.yml
00075|     needs:
00076|       - linux-jammy-py3_9-gcc11-build
00077|       - target-determination
00078|     with:
00079|       build-environment: linux-jammy-py3.9-gcc11
00080|       docker-image: ${{ needs.linux-jammy-py3_9-gcc11-build.outputs.docker-image }}
00081|       test-matrix: ${{ needs.linux-jammy-py3_9-gcc11-build.outputs.test-matrix }}
00082|     secrets: inherit
00083| 
00084|   linux-docs:
00085|     name: linux-docs
00086|     uses: ./.github/workflows/_docs.yml
00087|     needs: linux-jammy-py3_9-gcc11-build
00088|     with:
00089|       build-environment: linux-jammy-py3.9-gcc11
00090|       docker-image: ${{ needs.linux-jammy-py3_9-gcc11-build.outputs.docker-image }}
00091|     secrets: inherit
00092| 
00093|   linux-jammy-py3_9-gcc11-no-ops:
00094|     name: linux-jammy-py3.9-gcc11-no-ops
00095|     uses: ./.github/workflows/_linux-build.yml
00096|     needs: get-label-type
00097|     with:
00098|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00099|       build-environment: linux-jammy-py3.9-gcc11-no-ops
00100|       docker-image-name: pytorch-linux-jammy-py3.9-gcc11
00101|       test-matrix: |
00102|         { include: [
00103|           { config: "default", shard: 1, num_shards: 1 },
00104|         ]}
00105|     secrets: inherit
00106| 
00107|   linux-jammy-py3_9-gcc11-pch:
00108|     name: linux-jammy-py3.9-gcc11-pch
00109|     uses: ./.github/workflows/_linux-build.yml
00110|     needs: get-label-type
00111|     with:
00112|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00113|       build-environment: linux-jammy-py3.9-gcc11-pch
00114|       docker-image-name: pytorch-linux-jammy-py3.9-gcc11
00115|       test-matrix: |
00116|         { include: [
00117|           { config: "default", shard: 1, num_shards: 1 },
00118|         ]}
00119|     secrets: inherit
00120| 
00121|   linux-jammy-py3_10-clang15-asan-build:
00122|     name: linux-jammy-py3.10-clang15-asan
00123|     uses: ./.github/workflows/_linux-build.yml
00124|     needs: get-label-type
00125|     with:
00126|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00127|       build-environment: linux-jammy-py3.10-clang15-asan
00128|       docker-image-name: pytorch-linux-jammy-py3-clang15-asan
00129|       test-matrix: |
00130|         { include: [
00131|           { config: "default", shard: 1, num_shards: 6, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00132|           { config: "default", shard: 2, num_shards: 6, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00133|           { config: "default", shard: 3, num_shards: 6, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00134|           { config: "default", shard: 4, num_shards: 6, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00135|           { config: "default", shard: 5, num_shards: 6, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00136|           { config: "default", shard: 6, num_shards: 6, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00137|         ]}
00138|       sync-tag: asan-build
00139|     secrets: inherit
00140| 
00141| 
00142|   linux-jammy-py3_10-clang15-asan-test:
00143|     name: linux-jammy-py3.10-clang15-asan
00144|     uses: ./.github/workflows/_linux-test.yml
00145|     needs:
00146|       - linux-jammy-py3_10-clang15-asan-build
00147|       - target-determination
00148|     with:
00149|       build-environment: linux-jammy-py3.10-clang15-asan
00150|       docker-image: ${{ needs.linux-jammy-py3_10-clang15-asan-build.outputs.docker-image }}
00151|       test-matrix: ${{ needs.linux-jammy-py3_10-clang15-asan-build.outputs.test-matrix }}
00152|       sync-tag: asan-test
00153|     secrets: inherit
00154| 
00155|   linux-focal-py3_9-clang10-onnx-build:
00156|     name: linux-focal-py3.9-clang10-onnx
00157|     uses: ./.github/workflows/_linux-build.yml
00158|     needs: get-label-type
00159|     with:
00160|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00161|       build-environment: linux-focal-py3.9-clang10-onnx
00162|       docker-image-name: pytorch-linux-focal-py3-clang10-onnx
00163|       test-matrix: |
00164|         { include: [
00165|           { config: "default", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00166|           { config: "default", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00167|         ]}
00168|     secrets: inherit
00169| 
00170|   linux-focal-py3_9-clang10-onnx-test:
00171|     name: linux-focal-py3.9-clang10-onnx
00172|     uses: ./.github/workflows/_linux-test.yml
00173|     needs:
00174|       - linux-focal-py3_9-clang10-onnx-build
00175|       - target-determination
00176|     with:
00177|       build-environment: linux-focal-py3.9-clang10-onnx
00178|       docker-image: ${{ needs.linux-focal-py3_9-clang10-onnx-build.outputs.docker-image }}
00179|       test-matrix: ${{ needs.linux-focal-py3_9-clang10-onnx-build.outputs.test-matrix }}
00180|     secrets: inherit
00181| 
00182|   linux-focal-py3_9-clang10-build:
00183|     name: linux-focal-py3.9-clang10
00184|     uses: ./.github/workflows/_linux-build.yml
00185|     needs: get-label-type
00186|     with:
00187|       runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge"
00188|       build-environment: linux-focal-py3.9-clang10
00189|       docker-image-name: pytorch-linux-focal-py3.9-clang10
00190|       test-matrix: |
00191|         { include: [
00192|           { config: "default", shard: 1, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00193|           { config: "default", shard: 2, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00194|           { config: "default", shard: 3, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00195|           { config: "default", shard: 4, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00196|           { config: "default", shard: 5, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00197|           { config: "crossref", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00198|           { config: "crossref", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00199|           { config: "dynamo_wrapped", shard: 1, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00200|           { config: "dynamo_wrapped", shard: 2, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00201|           { config: "dynamo_wrapped", shard: 3, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00202|         ]}
00203|     secrets: inherit
00204| 
00205|   linux-focal-py3_9-clang10-test:
00206|     name: linux-focal-py3.9-clang10
00207|     uses: ./.github/workflows/_linux-test.yml
00208|     needs:
00209|       - linux-focal-py3_9-clang10-build
00210|       - target-determination
00211|     with:
00212|       build-environment: linux-focal-py3.9-clang10
00213|       docker-image: ${{ needs.linux-focal-py3_9-clang10-build.outputs.docker-image }}
00214|       test-matrix: ${{ needs.linux-focal-py3_9-clang10-build.outputs.test-matrix }}
00215|     secrets: inherit
00216| 
00217|   linux-focal-py3_11-clang10-build:
00218|     name: linux-focal-py3.11-clang10
00219|     uses: ./.github/workflows/_linux-build.yml
00220|     needs: get-label-type
00221|     with:
00222|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00223|       build-environment: linux-focal-py3.11-clang10
00224|       docker-image-name: pytorch-linux-focal-py3.11-clang10
00225|       test-matrix: |
00226|         { include: [
00227|           { config: "default", shard: 1, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00228|           { config: "default", shard: 2, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00229|           { config: "default", shard: 3, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00230|           { config: "default", shard: 4, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00231|           { config: "default", shard: 5, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00232|           { config: "crossref", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00233|           { config: "crossref", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00234|           { config: "dynamo_wrapped", shard: 1, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00235|           { config: "dynamo_wrapped", shard: 2, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00236|           { config: "dynamo_wrapped", shard: 3, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00237|         ]}
00238|     secrets: inherit
00239| 
00240|   linux-focal-py3_11-clang10-test:
00241|     name: linux-focal-py3.11-clang10
00242|     uses: ./.github/workflows/_linux-test.yml
00243|     needs:
00244|       - linux-focal-py3_11-clang10-build
00245|       - target-determination
00246|     with:
00247|       build-environment: linux-focal-py3.11-clang10
00248|       docker-image: ${{ needs.linux-focal-py3_11-clang10-build.outputs.docker-image }}
00249|       test-matrix: ${{ needs.linux-focal-py3_11-clang10-build.outputs.test-matrix }}
00250|     secrets: inherit
00251| 
00252|   linux-focal-py3_12-clang10-build:
00253|     name: linux-focal-py3.12-clang10
00254|     uses: ./.github/workflows/_linux-build.yml
00255|     needs: get-label-type
00256|     with:
00257|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00258|       build-environment: linux-focal-py3.12-clang10
00259|       docker-image-name: pytorch-linux-focal-py3.12-clang10
00260|       test-matrix: |
00261|         { include: [
00262|           { config: "default", shard: 1, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00263|           { config: "default", shard: 2, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00264|           { config: "default", shard: 3, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00265|           { config: "default", shard: 4, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00266|           { config: "default", shard: 5, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00267|           { config: "dynamo_wrapped", shard: 1, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00268|           { config: "dynamo_wrapped", shard: 2, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00269|           { config: "dynamo_wrapped", shard: 3, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00270|         ]}
00271|     secrets: inherit
00272| 
00273|   linux-focal-py3_12-clang10-test:
00274|     name: linux-focal-py3.12-clang10
00275|     uses: ./.github/workflows/_linux-test.yml
00276|     needs: linux-focal-py3_12-clang10-build
00277|     with:
00278|       build-environment: linux-focal-py3.12-clang10
00279|       docker-image: ${{ needs.linux-focal-py3_12-clang10-build.outputs.docker-image }}
00280|       test-matrix: ${{ needs.linux-focal-py3_12-clang10-build.outputs.test-matrix }}
00281|       timeout-minutes: 600
00282|     secrets: inherit
00283| 
00284|   linux-focal-py3_13-clang10-build:
00285|     name: linux-focal-py3.13-clang10
00286|     uses: ./.github/workflows/_linux-build.yml
00287|     needs: get-label-type
00288|     with:
00289|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00290|       build-environment: linux-focal-py3.13-clang10
00291|       docker-image-name: pytorch-linux-focal-py3.13-clang10
00292|       test-matrix: |
00293|         { include: [
00294|           { config: "default", shard: 1, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00295|           { config: "default", shard: 2, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00296|           { config: "default", shard: 3, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00297|           { config: "default", shard: 4, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00298|           { config: "default", shard: 5, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00299|           { config: "dynamo_wrapped", shard: 1, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00300|           { config: "dynamo_wrapped", shard: 2, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00301|           { config: "dynamo_wrapped", shard: 3, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00302|         ]}
00303|     secrets: inherit
00304| 
00305|   linux-focal-py3_13-clang10-test:
00306|     name: linux-focal-py3.13-clang10
00307|     uses: ./.github/workflows/_linux-test.yml
00308|     needs: linux-focal-py3_13-clang10-build
00309|     with:
00310|       build-environment: linux-focal-py3.13-clang10
00311|       docker-image: ${{ needs.linux-focal-py3_13-clang10-build.outputs.docker-image }}
00312|       test-matrix: ${{ needs.linux-focal-py3_13-clang10-build.outputs.test-matrix }}
00313|       timeout-minutes: 600
00314|     secrets: inherit
00315| 
00316|   linux-focal-cuda11_8-py3_10-gcc9-build:
00317|     name: linux-focal-cuda11.8-py3.10-gcc9
00318|     uses: ./.github/workflows/_linux-build.yml
00319|     needs: get-label-type
00320|     with:
00321|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00322|       build-environment: linux-focal-cuda11.8-py3.10-gcc9
00323|       docker-image-name: pytorch-linux-focal-cuda11.8-cudnn9-py3-gcc9
00324|       cuda-arch-list: '7.5'
00325|       test-matrix: |
00326|         { include: [
00327|           { config: "distributed", shard: 1, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g4dn.12xlarge.nvidia.gpu" },
00328|           { config: "distributed", shard: 2, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g4dn.12xlarge.nvidia.gpu" },
00329|           { config: "distributed", shard: 3, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g4dn.12xlarge.nvidia.gpu" },
00330|         ]}
00331|     secrets: inherit
00332| 
00333|   linux-focal-cuda11_8-py3_10-gcc9-test:
00334|     name: linux-focal-cuda11.8-py3.10-gcc9
00335|     uses: ./.github/workflows/_linux-test.yml
00336|     needs:
00337|       - linux-focal-cuda11_8-py3_10-gcc9-build
00338|       - target-determination
00339|     with:
00340|       timeout-minutes: 360
00341|       build-environment: linux-focal-cuda11.8-py3.10-gcc9
00342|       docker-image: ${{ needs.linux-focal-cuda11_8-py3_10-gcc9-build.outputs.docker-image }}
00343|       test-matrix: ${{ needs.linux-focal-cuda11_8-py3_10-gcc9-build.outputs.test-matrix }}
00344|     secrets: inherit
00345| 
00346|   linux-focal-cuda12_4-py3_10-gcc9-build:
00347|     name: linux-focal-cuda12.4-py3.10-gcc9
00348|     uses: ./.github/workflows/_linux-build.yml
00349|     needs: get-label-type
00350|     with:
00351|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00352|       build-environment: linux-focal-cuda12.4-py3.10-gcc9
00353|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9
00354|       test-matrix: |
00355|         { include: [
00356|           { config: "default", shard: 1, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00357|           { config: "default", shard: 2, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00358|           { config: "default", shard: 3, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00359|           { config: "default", shard: 4, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00360|           { config: "default", shard: 5, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00361|         ]}
00362|     secrets: inherit
00363| 
00364|   linux-focal-cuda12_4-py3_10-gcc9-test:
00365|     name: linux-focal-cuda12.4-py3.10-gcc9
00366|     uses: ./.github/workflows/_linux-test.yml
00367|     needs:
00368|       - linux-focal-cuda12_4-py3_10-gcc9-build
00369|       - target-determination
00370|     with:
00371|       timeout-minutes: 360
00372|       build-environment: linux-focal-cuda12.4-py3.10-gcc9
00373|       docker-image: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-build.outputs.docker-image }}
00374|       test-matrix: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-build.outputs.test-matrix }}
00375|     secrets: inherit
00376| 
00377|   linux-jammy-py3-clang12-mobile-build:
00378|     name: linux-jammy-py3-clang12-mobile-build
00379|     uses: ./.github/workflows/_linux-build.yml
00380|     needs: get-label-type
00381|     with:
00382|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00383|       build-environment: linux-jammy-py3-clang12-mobile-build
00384|       docker-image-name: pytorch-linux-jammy-py3-clang15-asan
00385|       build-generates-artifacts: false
00386|       test-matrix: |
00387|         { include: [
00388|           { config: "default", shard: 1, num_shards: 1 },
00389|         ]}
00390|     secrets: inherit
00391| 
00392|   linux-jammy-cuda-11_8-cudnn9-py3_9-clang12-build:
00393|     name: linux-jammy-cuda11.8-cudnn9-py3.9-clang12
00394|     uses: ./.github/workflows/_linux-build.yml
00395|     needs: get-label-type
00396|     with:
00397|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00398|       build-environment: linux-jammy-cuda11.8-cudnn9-py3.9-clang12
00399|       docker-image-name: pytorch-linux-jammy-cuda11.8-cudnn9-py3.9-clang12
00400|       test-matrix: |
00401|         { include: [
00402|           { config: "default", shard: 1, num_shards: 1 },
00403|         ]}
00404|     secrets: inherit
00405| 
00406|   linux-focal-py3_9-clang9-xla-build:
00407|     name: linux-focal-py3_9-clang9-xla
00408|     uses: ./.github/workflows/_linux-build.yml
00409|     needs: get-label-type
00410|     with:
00411|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00412|       build-environment: linux-focal-py3.9-clang9-xla
00413|       docker-image-name: 308535385114.dkr.ecr.us-east-1.amazonaws.com/pytorch/xla_base:v1.3-lite
00414|       test-matrix: |
00415|         { include: [
00416|           { config: "xla", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.12xlarge" },
00417|         ]}
00418|     secrets: inherit
00419| 
00420|   linux-focal-py3_9-clang9-xla-test:
00421|     name: linux-focal-py3_9-clang9-xla
00422|     uses: ./.github/workflows/_linux-test.yml
00423|     needs: linux-focal-py3_9-clang9-xla-build
00424|     with:
00425|       build-environment: linux-focal-py3.9-clang9-xla
00426|       docker-image: ${{ needs.linux-focal-py3_9-clang9-xla-build.outputs.docker-image }}
00427|       test-matrix: ${{ needs.linux-focal-py3_9-clang9-xla-build.outputs.test-matrix }}
00428|     secrets: inherit
00429| 
00430|   win-vs2019-cpu-py3-build:
00431|     # don't run build twice on main
00432|     if: github.event_name == 'pull_request'
00433|     name: win-vs2019-cpu-py3
00434|     uses: ./.github/workflows/_win-build.yml
00435|     needs: get-label-type
00436|     with:
00437|       build-environment: win-vs2019-cpu-py3
00438|       cuda-version: cpu
00439|       sync-tag: win-cpu-build
00440|       runner: "${{ needs.get-label-type.outputs.label-type }}windows.4xlarge.nonephemeral"
00441|       test-matrix: |
00442|         { include: [
00443|           { config: "default", shard: 1, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}windows.4xlarge.nonephemeral" },
00444|           { config: "default", shard: 2, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}windows.4xlarge.nonephemeral" },
00445|           { config: "default", shard: 3, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}windows.4xlarge.nonephemeral" },
00446|         ]}
00447|     secrets: inherit
00448| 
00449|   linux-focal-cpu-py3_10-gcc9-bazel-test:
00450|     name: linux-focal-cpu-py3.10-gcc9-bazel-test
00451|     uses: ./.github/workflows/_bazel-build-test.yml
00452|     needs: get-label-type
00453|     with:
00454|       runner: "${{ needs.get-label-type.outputs.label-type }}linux.large"
00455|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-bazel-test
00456|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9
00457|       cuda-version: cpu
00458|       test-matrix: |
00459|         { include: [
00460|           { config: "default", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00461|         ]}
00462|     secrets: inherit
00463| 
00464|   linux-jammy-py3_9-gcc11-mobile-lightweight-dispatch-build:
00465|     name: linux-jammy-py3.9-gcc11-mobile-lightweight-dispatch-build
00466|     uses: ./.github/workflows/_linux-build.yml
00467|     needs: get-label-type
00468|     with:
00469|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00470|       build-environment: linux-jammy-py3.9-gcc111-mobile-lightweight-dispatch-build
00471|       docker-image-name: pytorch-linux-jammy-py3.9-gcc11
00472|       build-generates-artifacts: false
00473|       test-matrix: |
00474|         { include: [
00475|           { config: "default", shard: 1, num_shards: 1 },
00476|         ]}
00477|     secrets: inherit
00478| 
00479|   linux-focal-rocm6_2-py3_10-build:
00480|     # don't run build twice on main
00481|     if: github.event_name == 'pull_request'
00482|     name: linux-focal-rocm6.2-py3.10
00483|     uses: ./.github/workflows/_linux-build.yml
00484|     needs: get-label-type
00485|     with:
00486|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00487|       build-environment: linux-focal-rocm6.2-py3.10
00488|       docker-image-name: pytorch-linux-focal-rocm-n-py3
00489|       sync-tag: rocm-build
00490|       test-matrix: |
00491|         { include: [
00492|           { config: "default", shard: 1, num_shards: 3, runner: "linux.rocm.gpu" },
00493|           { config: "default", shard: 2, num_shards: 3, runner: "linux.rocm.gpu" },
00494|           { config: "default", shard: 3, num_shards: 3, runner: "linux.rocm.gpu" },
00495|         ]}
00496|     secrets: inherit
00497| 
00498|   linux-focal-cuda12_4-py3_10-gcc9-sm89-build:
00499|     name: linux-focal-cuda12.4-py3.10-gcc9-sm89
00500|     uses: ./.github/workflows/_linux-build.yml
00501|     needs: get-label-type
00502|     with:
00503|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00504|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-sm89
00505|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9
00506|       cuda-arch-list: 8.9
00507|       test-matrix: |
00508|         { include: [
00509|           { config: "default", shard: 1, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g6.4xlarge.experimental.nvidia.gpu" },
00510|           { config: "default", shard: 2, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g6.4xlarge.experimental.nvidia.gpu" },
00511|           { config: "default", shard: 3, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g6.4xlarge.experimental.nvidia.gpu" },
00512|           { config: "default", shard: 4, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g6.4xlarge.experimental.nvidia.gpu" },
00513|           { config: "default", shard: 5, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g6.4xlarge.experimental.nvidia.gpu" },
00514|         ]}
00515|     secrets: inherit
00516| 
00517|   linux-focal-cuda12_4-py3_10-gcc9-sm89-test:
00518|     name: linux-focal-cuda12.4-py3.10-gcc9-sm89
00519|     uses: ./.github/workflows/_linux-test.yml
00520|     needs:
00521|       - linux-focal-cuda12_4-py3_10-gcc9-sm89-build
00522|       - target-determination
00523|     with:
00524|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-sm89
00525|       docker-image: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-sm89-build.outputs.docker-image }}
00526|       test-matrix: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-sm89-build.outputs.test-matrix }}
00527|     secrets: inherit
00528| 
00529|   linux-jammy-py3-clang12-executorch-build:
00530|     name: linux-jammy-py3-clang12-executorch
00531|     uses: ./.github/workflows/_linux-build.yml
00532|     needs: get-label-type
00533|     with:
00534|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00535|       build-environment: linux-jammy-py3-clang12-executorch
00536|       docker-image-name: pytorch-linux-jammy-py3-clang12-executorch
00537|       test-matrix: |
00538|         { include: [
00539|           { config: "executorch", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge" },
00540|         ]}
00541|     secrets: inherit
00542| 
00543|   linux-jammy-py3-clang12-executorch-test:
00544|     name: linux-jammy-py3-clang12-executorch
00545|     uses: ./.github/workflows/_linux-test.yml
00546|     needs: linux-jammy-py3-clang12-executorch-build
00547|     with:
00548|       build-environment: linux-jammy-py3-clang12-executorch
00549|       docker-image: ${{ needs.linux-jammy-py3-clang12-executorch-build.outputs.docker-image }}
00550|       test-matrix: ${{ needs.linux-jammy-py3-clang12-executorch-build.outputs.test-matrix }}
00551|     secrets: inherit
00552| 
00553|   linux-focal-py3_12-clang10-experimental-split-build:
00554|     if: false # See https://github.com/pytorch/pytorch/issues/138750
00555|     name: linux-focal-py3.12-clang10-experimental-split-build
00556|     uses: ./.github/workflows/_linux-build.yml
00557|     needs: get-label-type
00558|     with:
00559|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00560|       use_split_build: True
00561|       build-environment: linux-focal-py3.12-clang10
00562|       docker-image-name: pytorch-linux-focal-py3.12-clang10
00563|       test-matrix: |
00564|         { include: [
00565|           { config: "default", shard: 1, num_shards: 3, runner: "linux.4xlarge" },
00566|           { config: "default", shard: 2, num_shards: 3, runner: "linux.4xlarge" },
00567|           { config: "default", shard: 3, num_shards: 3, runner: "linux.4xlarge" },
00568|           { config: "dynamo_wrapped", shard: 1, num_shards: 3, runner: "linux.2xlarge" },
00569|           { config: "dynamo_wrapped", shard: 2, num_shards: 3, runner: "linux.2xlarge" },
00570|           { config: "dynamo_wrapped", shard: 3, num_shards: 3, runner: "linux.2xlarge" },
00571|         ]}
00572|     secrets: inherit
00573| 
00574|   linux-focal-py3_12-clang10-experimental-split-build-test:
00575|     name: linux-focal-py3.12-clang10-experimental-split-build
00576|     uses: ./.github/workflows/_linux-test.yml
00577|     needs: linux-focal-py3_12-clang10-experimental-split-build
00578|     with:
00579|       build-environment: linux-focal-py3.12-clang10-experimental-split-build
00580|       docker-image: ${{ needs.linux-focal-py3_12-clang10-experimental-split-build.outputs.docker-image }}
00581|       test-matrix: ${{ needs.linux-focal-py3_12-clang10-experimental-split-build.outputs.test-matrix }}
00582|       timeout-minutes: 600
00583|     secrets: inherit
00584| 
00585|   linux-focal-cuda12_4-py3_10-gcc9-inductor-build:
00586|     name: cuda12.4-py3.10-gcc9-sm75
00587|     uses: ./.github/workflows/_linux-build.yml
00588|     needs: get-label-type
00589|     with:
00590|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00591|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-sm75
00592|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9-inductor-benchmarks
00593|       cuda-arch-list: '7.5'
00594|       test-matrix: |
00595|         { include: [
00596|           { config: "pr_time_benchmarks", shard: 1, num_shards: 1, runner: "linux.g4dn.metal.nvidia.gpu" },
00597|         ]}
00598|     secrets: inherit
00599| 
00600|   linux-focal-cuda12_4-py3_10-gcc9-inductor-test:
00601|     name: cuda12.4-py3.10-gcc9-sm75
00602|     uses: ./.github/workflows/_linux-test.yml
00603|     needs: linux-focal-cuda12_4-py3_10-gcc9-inductor-build
00604|     with:
00605|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-sm75
00606|       docker-image: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-inductor-build.outputs.docker-image }}
00607|       test-matrix: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-inductor-build.outputs.test-matrix }}
00608|     secrets: inherit
00609| 

(End of file - total 609 lines)
</file>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\trunk.yml"
}
```

**Output:**
```
<file>
00001| name: trunk
00002| 
00003| on:
00004|   push:
00005|     branches:
00006|       - main
00007|       - release/*
00008|       - landchecks/*
00009|     tags:
00010|       - ciflow/trunk/*
00011|   workflow_dispatch:
00012|   schedule:
00013|     - cron: 29 8 * * *  # about 1:29am PDT
00014| 
00015| concurrency:
00016|   group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref_name }}-${{ github.ref_type == 'branch' && github.sha }}-${{ github.event_name == 'workflow_dispatch' }}-${{ github.event_name == 'schedule' }}
00017|   cancel-in-progress: true
00018| 
00019| permissions: read-all
00020| 
00021| jobs:
00022|   llm-td:
00023|     if: github.repository_owner == 'pytorch'
00024|     name: before-test
00025|     uses: ./.github/workflows/llm_td_retrieval.yml
00026|     permissions:
00027|       id-token: write
00028|       contents: read
00029| 
00030|   target-determination:
00031|     name: before-test
00032|     uses: ./.github/workflows/target_determination.yml
00033|     needs: llm-td
00034|     permissions:
00035|       id-token: write
00036|       contents: read
00037| 
00038|   get-label-type:
00039|     name: get-label-type
00040|     uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
00041|     if: ${{ (github.event_name != 'schedule' || github.repository == 'pytorch/pytorch') && github.repository_owner == 'pytorch' }}
00042|     with:
00043|       triggering_actor: ${{ github.triggering_actor }}
00044|       issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
00045|       curr_branch: ${{ github.head_ref || github.ref_name }}
00046|       curr_ref_type: ${{ github.ref_type }}
00047| 
00048|   libtorch-linux-focal-cuda12_1-py3_7-gcc9-debug-build:
00049|     name: libtorch-linux-focal-cuda12.1-py3.7-gcc9-debug
00050|     uses: ./.github/workflows/_linux-build.yml
00051|     needs: get-label-type
00052|     with:
00053|       build-environment: libtorch-linux-focal-cuda12.1-py3.7-gcc9
00054|       docker-image-name: pytorch-linux-focal-cuda12.1-cudnn9-py3-gcc9
00055|       build-generates-artifacts: false
00056|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00057|       runner: "linux.4xlarge"
00058|       test-matrix: |
00059|         { include: [
00060|           { config: "default", shard: 1, num_shards: 1 },
00061|         ]}
00062|     secrets: inherit
00063| 
00064|   # no-ops builds test USE_PER_OPERATOR_HEADERS=0 where ATen/ops is not generated
00065|   linux-focal-cuda12_1-py3_10-gcc9-no-ops-build:
00066|     name: linux-focal-cuda12.1-py3.10-gcc9-no-ops
00067|     uses: ./.github/workflows/_linux-build.yml
00068|     needs: get-label-type
00069|     with:
00070|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00071|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-no-ops
00072|       docker-image-name: pytorch-linux-focal-cuda12.1-cudnn9-py3-gcc9
00073|       test-matrix: |
00074|         { include: [
00075|           { config: "default", shard: 1, num_shards: 1 },
00076|         ]}
00077|     secrets: inherit
00078| 
00079|   libtorch-linux-focal-cuda12_4-py3_7-gcc9-debug-build:
00080|     name: libtorch-linux-focal-cuda12.4-py3.7-gcc9-debug
00081|     uses: ./.github/workflows/_linux-build.yml
00082|     needs: get-label-type
00083|     with:
00084|       build-environment: libtorch-linux-focal-cuda12.4-py3.7-gcc9
00085|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9
00086|       build-generates-artifacts: false
00087|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00088|       runner: "linux.4xlarge"
00089|       test-matrix: |
00090|         { include: [
00091|           { config: "default", shard: 1, num_shards: 1 },
00092|         ]}
00093|     secrets: inherit
00094| 
00095|   # no-ops builds test USE_PER_OPERATOR_HEADERS=0 where ATen/ops is not generated
00096|   linux-focal-cuda12_4-py3_10-gcc9-no-ops-build:
00097|     name: linux-focal-cuda12.4-py3.10-gcc9-no-ops
00098|     uses: ./.github/workflows/_linux-build.yml
00099|     needs: get-label-type
00100|     with:
00101|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00102|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-no-ops
00103|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9
00104|       test-matrix: |
00105|         { include: [
00106|           { config: "default", shard: 1, num_shards: 1 },
00107|         ]}
00108|     secrets: inherit
00109| 
00110|   macos-py3-arm64-build:
00111|     if: github.repository_owner == 'pytorch'
00112|     name: macos-py3-arm64
00113|     uses: ./.github/workflows/_mac-build.yml
00114|     with:
00115|       sync-tag: macos-py3-arm64-build
00116|       build-environment: macos-py3-arm64
00117|       runner-type: macos-m1-stable
00118|       build-generates-artifacts: true
00119|       # To match the one pre-installed in the m1 runners
00120|       python-version: 3.9.12
00121|       test-matrix: |
00122|         { include: [
00123|           { config: "default", shard: 1, num_shards: 3, runner: "macos-m1-stable" },
00124|           { config: "default", shard: 2, num_shards: 3, runner: "macos-m1-stable" },
00125|           { config: "default", shard: 3, num_shards: 3, runner: "macos-m1-stable" },
00126|         ]}
00127|     secrets: inherit
00128| 
00129|   macos-py3-arm64-mps-test:
00130|     name: macos-py3-arm64-mps
00131|     uses: ./.github/workflows/_mac-test-mps.yml
00132|     needs: macos-py3-arm64-build
00133|     if: needs.macos-py3-arm64-build.outputs.build-outcome == 'success'
00134|     with:
00135|       sync-tag: macos-py3-arm64-mps-test
00136|       build-environment: macos-py3-arm64
00137|       # Same as the build job
00138|       python-version: 3.9.12
00139|       test-matrix: |
00140|         { include: [
00141|           { config: "mps", shard: 1, num_shards: 1, runner: "macos-m1-13" },
00142|           { config: "mps", shard: 1, num_shards: 1, runner: "macos-m1-14" },
00143|         ]}
00144|     secrets: inherit
00145| 
00146|   macos-py3-arm64-test:
00147|     name: macos-py3-arm64
00148|     uses: ./.github/workflows/_mac-test.yml
00149|     needs:
00150|       - macos-py3-arm64-build
00151|       - target-determination
00152|     with:
00153|       build-environment: macos-py3-arm64
00154|       # Same as the build job
00155|       python-version: 3.9.12
00156|       test-matrix: ${{ needs.macos-py3-arm64-build.outputs.test-matrix }}
00157|     secrets: inherit
00158| 
00159|   win-vs2019-cpu-py3-build:
00160|     name: win-vs2019-cpu-py3
00161|     uses: ./.github/workflows/_win-build.yml
00162|     needs: get-label-type
00163|     with:
00164|       build-environment: win-vs2019-cpu-py3
00165|       cuda-version: cpu
00166|       sync-tag: win-cpu-build
00167|       runner: "${{ needs.get-label-type.outputs.label-type }}windows.4xlarge.nonephemeral"
00168|       test-matrix: |
00169|         { include: [
00170|           { config: "default", shard: 1, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}windows.4xlarge.nonephemeral" },
00171|           { config: "default", shard: 2, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}windows.4xlarge.nonephemeral" },
00172|           { config: "default", shard: 3, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}windows.4xlarge.nonephemeral" },
00173|         ]}
00174|     secrets: inherit
00175| 
00176|   win-vs2019-cpu-py3-test:
00177|     name: win-vs2019-cpu-py3
00178|     uses: ./.github/workflows/_win-test.yml
00179|     needs:
00180|       - win-vs2019-cpu-py3-build
00181|       - target-determination
00182|     with:
00183|       build-environment: win-vs2019-cpu-py3
00184|       cuda-version: cpu
00185|       test-matrix: ${{ needs.win-vs2019-cpu-py3-build.outputs.test-matrix }}
00186|     secrets: inherit
00187| 
00188|   win-vs2019-cuda12_1-py3-build:
00189|     name: win-vs2019-cuda12.1-py3
00190|     uses: ./.github/workflows/_win-build.yml
00191|     needs: get-label-type
00192|     with:
00193|       build-environment: win-vs2019-cuda12.1-py3
00194|       cuda-version: "12.1"
00195|       runner: "${{ needs.get-label-type.outputs.label-type }}windows.4xlarge.nonephemeral"
00196|     secrets: inherit
00197| 
00198|   linux-focal-rocm6_2-py3_10-build:
00199|     name: linux-focal-rocm6.2-py3.10
00200|     uses: ./.github/workflows/_linux-build.yml
00201|     needs: get-label-type
00202|     with:
00203|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00204|       build-environment: linux-focal-rocm6.2-py3.10
00205|       docker-image-name: pytorch-linux-focal-rocm-n-py3
00206|       sync-tag: rocm-build
00207|       test-matrix: |
00208|         { include: [
00209|           { config: "default", shard: 1, num_shards: 2, runner: "linux.rocm.gpu" },
00210|           { config: "default", shard: 2, num_shards: 2, runner: "linux.rocm.gpu" },
00211|           { config: "distributed", shard: 1, num_shards: 1, runner: "linux.rocm.gpu" },
00212|         ]}
00213|     secrets: inherit
00214| 
00215|   linux-focal-rocm6_2-py3_10-test:
00216|     permissions:
00217|       id-token: write
00218|       contents: read
00219|     name: linux-focal-rocm6.2-py3.10
00220|     uses: ./.github/workflows/_rocm-test.yml
00221|     needs:
00222|       - linux-focal-rocm6_2-py3_10-build
00223|       - target-determination
00224|     with:
00225|       build-environment: linux-focal-rocm6.2-py3.10
00226|       docker-image: ${{ needs.linux-focal-rocm6_2-py3_10-build.outputs.docker-image }}
00227|       test-matrix: ${{ needs.linux-focal-rocm6_2-py3_10-build.outputs.test-matrix }}
00228|       tests-to-include: "test_nn test_torch test_cuda test_ops test_unary_ufuncs test_binary_ufuncs test_autograd inductor/test_torchinductor distributed/test_c10d_common distributed/test_c10d_nccl"
00229|     secrets: inherit
00230| 
00231|   linux-focal-cuda12_4-py3_10-gcc9-experimental-split-build:
00232|     if: false # See https://github.com/pytorch/pytorch/issues/138750
00233|     name: linux-focal-cuda12.4-py3.10-gcc9-experimental-split-build
00234|     uses: ./.github/workflows/_linux-build.yml
00235|     needs: get-label-type
00236|     with:
00237|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00238|       use_split_build: true
00239|       build-environment: linux-focal-cuda12.4-py3.10-gcc9
00240|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9
00241|       test-matrix: |
00242|         { include: [
00243|           { config: "nogpu_AVX512", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00244|           { config: "nogpu_AVX512", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00245|           { config: "nogpu_NO_AVX2", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00246|           { config: "nogpu_NO_AVX2", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00247|           { config: "jit_legacy", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00248|           { config: "default", shard: 1, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00249|           { config: "default", shard: 2, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00250|           { config: "default", shard: 3, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00251|           { config: "default", shard: 4, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00252|           { config: "default", shard: 5, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00253|         ]}
00254|     secrets: inherit
00255| 
00256|   linux-focal-cuda12_4-py3_10-gcc9-experimental-split-build-test:
00257|     name: linux-focal-cuda12.4-py3.10-gcc9-experimental-split-build-test
00258|     uses: ./.github/workflows/_linux-test.yml
00259|     needs:
00260|       - linux-focal-cuda12_4-py3_10-gcc9-experimental-split-build
00261|       - target-determination
00262|     with:
00263|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-experimental-split-build
00264|       docker-image: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-experimental-split-build.outputs.docker-image }}
00265|       test-matrix: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-experimental-split-build.outputs.test-matrix }}
00266|     secrets: inherit
00267| 
00268|   # NB: Keep this in sync with inductor-perf-test-nightly.yml
00269|   linux-focal-cuda12_1-py3_10-gcc9-inductor-build:
00270|     name: cuda12.1-py3.10-gcc9-sm80
00271|     uses: ./.github/workflows/_linux-build.yml
00272|     needs: get-label-type
00273|     with:
00274|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-sm80
00275|       docker-image-name: pytorch-linux-focal-cuda12.1-cudnn9-py3-gcc9-inductor-benchmarks
00276|       cuda-arch-list: '8.0'
00277|     secrets: inherit
00278| 

(End of file - total 278 lines)
</file>
```

---

## Assistant (Build · openrouter/pony-alpha · 92.1s)

_Thinking:_

Now let me read some key reusable workflows (prefixed with _) and the templates directory to understand the architecture better.

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\_linux-build.yml"
}
```

**Output:**
```
<file>
00001| name: linux-build
00002| 
00003| on:
00004|   workflow_call:
00005|     inputs:
00006|       build-environment:
00007|         required: true
00008|         type: string
00009|         description: Top-level label for what's being built/tested.
00010|       docker-image-name:
00011|         required: true
00012|         type: string
00013|         description: Name of the base docker image to build with.
00014|       build-generates-artifacts:
00015|         required: false
00016|         type: boolean
00017|         default: true
00018|         description: If set, upload generated build artifacts.
00019|       build-with-debug:
00020|         required: false
00021|         type: boolean
00022|         default: false
00023|         description: If set, build in debug mode.
00024|       sync-tag:
00025|         required: false
00026|         type: string
00027|         default: ""
00028|         description: |
00029|           If this is set, our linter will use this to make sure that every other
00030|           job with the same `sync-tag` is identical.
00031|       cuda-arch-list:
00032|         required: false
00033|         type: string
00034|         default: "5.2"
00035|         description: |
00036|           List of CUDA architectures CI build should target.
00037|       runner_prefix:
00038|         required: false
00039|         default: ""
00040|         type: string
00041|         description: Prefix for runner label
00042|       runner:
00043|         required: false
00044|         type: string
00045|         default: "linux.2xlarge"
00046|         description: |
00047|           Label of the runner this job should run on.
00048|       test-matrix:
00049|         required: false
00050|         type: string
00051|         description: |
00052|           An option JSON description of what test configs to run later on. This
00053|           is moved here from the Linux test workflow so that we can apply filter
00054|           logic using test-config labels earlier and skip unnecessary builds
00055|       selected-test-configs:
00056|         description: |
00057|           A comma-separated list of test configurations from the test matrix to keep,
00058|           The empty list means we are going to keep every configurations by defaults
00059|         required: false
00060|         type: string
00061|         default: ""
00062|       s3-bucket:
00063|         description: S3 bucket to download artifact
00064|         required: false
00065|         type: string
00066|         default: "gha-artifacts"
00067|       aws-role-to-assume:
00068|         description: Role to assume for downloading artifacts
00069|         required: false
00070|         type: string
00071|         default: ""
00072|       use_split_build:
00073|         description: |
00074|           [Experimental] Build a libtorch only wheel and build pytorch such that
00075|           are built from the libtorch wheel.
00076|         required: false
00077|         type: boolean
00078|         default: false
00079| 
00080|     secrets:
00081|       HUGGING_FACE_HUB_TOKEN:
00082|         required: false
00083|         description: |
00084|           HF Auth token to avoid rate limits when downloading models or datasets from hub
00085|       SCRIBE_GRAPHQL_ACCESS_TOKEN:
00086|         required: false
00087|         description: |
00088|           FB app token to write to scribe endpoint
00089| 
00090| 
00091|     outputs:
00092|       docker-image:
00093|         value: ${{ jobs.build.outputs.docker-image }}
00094|         description: The docker image containing the built PyTorch.
00095|       test-matrix:
00096|         value: ${{ jobs.build.outputs.test-matrix }}
00097|         description: An optional JSON description of what test configs to run later on.
00098| 
00099| jobs:
00100|   build:
00101|     environment: ${{ github.ref == 'refs/heads/main' && 'scribe-protected' || startsWith(github.ref, 'refs/heads/release/') && 'scribe-protected' || contains(github.event.pull_request.labels.*.name, 'ci-scribe') && 'scribe-pr' || '' }}
00102|     # Don't run on forked repos
00103|     if: github.repository_owner == 'pytorch'
00104|     runs-on: ${{ inputs.runner_prefix}}${{ inputs.runner }}
00105|     timeout-minutes: 240
00106|     outputs:
00107|       docker-image: ${{ steps.calculate-docker-image.outputs.docker-image }}
00108|       test-matrix: ${{ steps.filter.outputs.test-matrix }}
00109|     steps:
00110|       - name: Setup SSH (Click me for login details)
00111|         uses: pytorch/test-infra/.github/actions/setup-ssh@release/2.6
00112|         if: inputs.build-environment != 'linux-s390x-binary-manywheel'
00113|         with:
00114|           github-secret: ${{ secrets.GITHUB_TOKEN }}
00115| 
00116|       # [pytorch repo ref]
00117|       # Use a pytorch/pytorch reference instead of a reference to the local
00118|       # checkout because when we run this action we don't *have* a local
00119|       # checkout. In other cases you should prefer a local checkout.
00120|       - name: Checkout PyTorch
00121|         uses: pytorch/pytorch/.github/actions/checkout-pytorch@release/2.6
00122|         with:
00123|           no-sudo: true
00124| 
00125|       - name: Setup Linux
00126|         uses: ./.github/actions/setup-linux
00127|         if: inputs.build-environment != 'linux-s390x-binary-manywheel'
00128| 
00129|       - name: configure aws credentials
00130|         uses: aws-actions/configure-aws-credentials@v3
00131|         if: ${{ inputs.aws-role-to-assume != '' && inputs.build-environment != 'linux-s390x-binary-manywheel' }}
00132|         with:
00133|           role-to-assume: ${{ inputs.aws-role-to-assume }}
00134|           role-session-name: gha-linux-build
00135|           aws-region: us-east-1
00136| 
00137|       - name: Calculate docker image
00138|         id: calculate-docker-image
00139|         uses: pytorch/test-infra/.github/actions/calculate-docker-image@release/2.6
00140|         if: inputs.build-environment != 'linux-s390x-binary-manywheel'
00141|         with:
00142|           docker-image-name: ${{ inputs.docker-image-name }}
00143| 
00144|       - name: Use following to pull public copy of the image
00145|         id: print-ghcr-mirror
00146|         if: inputs.build-environment != 'linux-s390x-binary-manywheel'
00147|         env:
00148|           ECR_DOCKER_IMAGE: ${{ steps.calculate-docker-image.outputs.docker-image }}
00149|         shell: bash
00150|         run: |
00151|           tag=${ECR_DOCKER_IMAGE##*/}
00152|           echo "docker pull ghcr.io/pytorch/ci-image:${tag/:/-}"
00153| 
00154|       - name: Pull docker image
00155|         uses: pytorch/test-infra/.github/actions/pull-docker-image@release/2.6
00156|         if: inputs.build-environment != 'linux-s390x-binary-manywheel'
00157|         with:
00158|           docker-image: ${{ steps.calculate-docker-image.outputs.docker-image }}
00159| 
00160|       - name: Parse ref
00161|         id: parse-ref
00162|         run: .github/scripts/parse_ref.py
00163| 
00164|       - name: Get workflow job id
00165|         id: get-job-id
00166|         uses: ./.github/actions/get-workflow-job-id
00167|         if: always()
00168|         with:
00169|           github-token: ${{ secrets.GITHUB_TOKEN }}
00170| 
00171|       # Apply the filter logic to the build step too if the test-config label is already there
00172|       - name: Select all requested test configurations (if the test matrix is available)
00173|         id: filter
00174|         uses: ./.github/actions/filter-test-configs
00175|         with:
00176|           github-token: ${{ secrets.GITHUB_TOKEN }}
00177|           test-matrix: ${{ inputs.test-matrix }}
00178|           selected-test-configs: ${{ inputs.selected-test-configs }}
00179|           job-name: ${{ steps.get-job-id.outputs.job-name }}
00180| 
00181|       - name: Download pytest cache
00182|         uses: ./.github/actions/pytest-cache-download
00183|         continue-on-error: true
00184|         if: inputs.build-environment != 'linux-s390x-binary-manywheel'
00185|         with:
00186|           cache_dir: .pytest_cache
00187|           job_identifier: ${{ github.workflow }}_${{ inputs.build-environment }}
00188|           s3_bucket: ${{ inputs.s3-bucket }}
00189| 
00190|       - name: Build
00191|         if: steps.filter.outputs.is-test-matrix-empty == 'False' || inputs.test-matrix == ''
00192|         id: build
00193|         env:
00194|           BUILD_ENVIRONMENT: ${{ inputs.build-environment }}
00195|           BRANCH: ${{ steps.parse-ref.outputs.branch }}
00196|           # TODO duplicated
00197|           AWS_DEFAULT_REGION: us-east-1
00198|           PR_NUMBER: ${{ github.event.pull_request.number }}
00199|           SHA1: ${{ github.event.pull_request.head.sha || github.sha }}
00200|           SCCACHE_BUCKET: ossci-compiler-cache-circleci-v2
00201|           SCCACHE_REGION: us-east-1
00202|           SCCACHE_S3_KEY_PREFIX: ${{ github.workflow }}
00203|           XLA_CLANG_CACHE_S3_BUCKET_NAME: ossci-compiler-clang-cache-circleci-xla
00204|           PR_LABELS: ${{ toJson(github.event.pull_request.labels.*.name) }}
00205|           TORCH_CUDA_ARCH_LIST: ${{ inputs.cuda-arch-list }}
00206|           DOCKER_IMAGE: ${{ steps.calculate-docker-image.outputs.docker-image }}
00207|           DOCKER_IMAGE_S390X: ${{ inputs.docker-image-name }}
00208|           XLA_CUDA: ${{ contains(inputs.build-environment, 'xla') && '0' || '' }}
00209|           DEBUG: ${{ inputs.build-with-debug && '1' || '0' }}
00210|           OUR_GITHUB_JOB_ID: ${{ steps.get-job-id.outputs.job-id }}
00211|           HUGGING_FACE_HUB_TOKEN: ${{ secrets.HUGGING_FACE_HUB_TOKEN }}
00212|           SCRIBE_GRAPHQL_ACCESS_TOKEN: ${{ secrets.SCRIBE_GRAPHQL_ACCESS_TOKEN }}
00213|           USE_SPLIT_BUILD: ${{ inputs.use_split_build }}
00214|         run: |
00215|           START_TIME=$(date +%s)
00216|           if [[ ${BUILD_ENVIRONMENT} == *"s390x"* ]]; then
00217|             JENKINS_USER=
00218|             USED_IMAGE="${DOCKER_IMAGE_S390X}"
00219| 
00220|             # since some steps are skipped on s390x, if they are necessary, run them here
00221|             env | grep '^GITHUB' >> "/tmp/github_env_${GITHUB_RUN_ID}"
00222|             env | grep '^CI' >> "/tmp/github_env_${GITHUB_RUN_ID}"
00223|           else
00224|             JENKINS_USER="--user jenkins"
00225|             USED_IMAGE="${DOCKER_IMAGE}"
00226|           fi
00227| 
00228|           # Leaving 1GB for the runner and other things
00229|           TOTAL_AVAILABLE_MEMORY_IN_GB=$(awk '/MemTotal/ { printf "%.3f \n", $2/1024/1024 - 1 }' /proc/meminfo)
00230|           # https://docs.docker.com/engine/containers/resource_constraints/#--memory-swap-details
00231|           TOTAL_MEMORY_WITH_SWAP=$(("${TOTAL_AVAILABLE_MEMORY_IN_GB%.*}" * 2))
00232| 
00233|           # detached container should get cleaned up by teardown_ec2_linux
00234|           # Used for JENKINS_USER, which can be empty
00235|           # shellcheck disable=SC2086
00236|           container_name=$(docker run \
00237|             -e BUILD_ENVIRONMENT \
00238|             -e MAX_JOBS="$(nproc --ignore=2)" \
00239|             -e AWS_DEFAULT_REGION \
00240|             -e PR_NUMBER \
00241|             -e SHA1 \
00242|             -e BRANCH \
00243|             -e SCCACHE_BUCKET \
00244|             -e SCCACHE_REGION \
00245|             -e SCCACHE_S3_KEY_PREFIX \
00246|             -e XLA_CUDA \
00247|             -e XLA_CLANG_CACHE_S3_BUCKET_NAME \
00248|             -e SKIP_SCCACHE_INITIALIZATION=1 \
00249|             -e TORCH_CUDA_ARCH_LIST \
00250|             -e PR_LABELS \
00251|             -e OUR_GITHUB_JOB_ID \
00252|             -e HUGGING_FACE_HUB_TOKEN \
00253|             -e SCRIBE_GRAPHQL_ACCESS_TOKEN \
00254|             -e USE_SPLIT_BUILD \
00255|             --memory="${TOTAL_AVAILABLE_MEMORY_IN_GB%.*}g" \
00256|             --memory-swap="${TOTAL_MEMORY_WITH_SWAP}g" \
00257|             --env-file="/tmp/github_env_${GITHUB_RUN_ID}" \
00258|             --security-opt seccomp=unconfined \
00259|             --cap-add=SYS_PTRACE \
00260|             --tty \
00261|             --detach \
00262|             ${JENKINS_USER} \
00263|             -v "${GITHUB_WORKSPACE}:/var/lib/jenkins/workspace" \
00264|             -w /var/lib/jenkins/workspace \
00265|             "${USED_IMAGE}"
00266|           )
00267|           docker exec -t "${container_name}" sh -c '.ci/pytorch/build.sh'
00268| 
00269|           END_TIME=$(date +%s)
00270|           echo "build_time=$((END_TIME - START_TIME))" >> "$GITHUB_OUTPUT"
00271| 
00272|       - name: Archive artifacts into zip
00273|         if: inputs.build-generates-artifacts && steps.build.outcome != 'skipped'
00274|         run: |
00275|           zip -1 -r artifacts.zip dist/ build/custom_test_artifacts build/lib build/bin .additional_ci_files
00276| 
00277|       - name: Store PyTorch Build Artifacts on S3
00278|         uses: seemethere/upload-artifact-s3@v5
00279|         if: inputs.build-generates-artifacts && steps.build.outcome != 'skipped' && !inputs.use_split_build && inputs.build-environment != 'linux-s390x-binary-manywheel'
00280|         with:
00281|           name: ${{ inputs.build-environment }}
00282|           retention-days: 14
00283|           if-no-files-found: error
00284|           path: artifacts.zip
00285|           s3-bucket: ${{ inputs.s3-bucket }}
00286| 
00287|       - name: Store PyTorch Build Artifacts on S3 for split build
00288|         uses: seemethere/upload-artifact-s3@v5
00289|         if: inputs.build-generates-artifacts && steps.build.outcome != 'skipped' && inputs.use_split_build && inputs.build-environment != 'linux-s390x-binary-manywheel'
00290|         with:
00291|           name: ${{ inputs.build-environment }}-experimental-split-build
00292|           retention-days: 14
00293|           if-no-files-found: error
00294|           path: artifacts.zip
00295|           s3-bucket: ${{ inputs.s3-bucket }}
00296| 
00297|       - name: Store PyTorch Build Artifacts for s390x
00298|         uses: actions/upload-artifact@v4
00299|         if: inputs.build-generates-artifacts && steps.build.outcome != 'skipped' && !inputs.use_split_build && inputs.build-environment == 'linux-s390x-binary-manywheel'
00300|         with:
00301|           name: ${{ inputs.build-environment }}
00302|           retention-days: 14
00303|           if-no-files-found: error
00304|           path: artifacts.zip
00305| 
00306|       - name: Store PyTorch Build Artifacts for s390x for split build
00307|         uses: actions/upload-artifact@v4
00308|         if: inputs.build-generates-artifacts && steps.build.outcome != 'skipped' && inputs.use_split_build && inputs.build-environment == 'linux-s390x-binary-manywheel'
00309|         with:
00310|           name: ${{ inputs.build-environment }}-experimental-split-build
00311|           retention-days: 14
00312|           if-no-files-found: error
00313|           path: artifacts.zip
00314| 
00315|       - name: Upload sccache stats
00316|         if: steps.build.outcome != 'skipped' && inputs.build-environment != 'linux-s390x-binary-manywheel'
00317|         uses: ./.github/actions/upload-sccache-stats
00318|         with:
00319|           github-token: ${{ secrets.GITHUB_TOKEN }}
00320|           build-time: ${{ steps.build.outputs.build_time }}
00321| 
00322|       - name: Teardown Linux
00323|         uses: pytorch/test-infra/.github/actions/teardown-linux@release/2.6
00324|         if: always() && inputs.build-environment != 'linux-s390x-binary-manywheel'
00325| 
00326|       - name: Cleanup docker
00327|         if: always() && inputs.build-environment == 'linux-s390x-binary-manywheel'
00328|         shell: bash
00329|         run: |
00330|           # on s390x stop the container for clean worker stop
00331|           # ignore expansion of "docker ps -q" since it could be empty
00332|           # shellcheck disable=SC2046
00333|           docker stop $(docker ps -q) || true
00334| 

(End of file - total 334 lines)
</file>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\_linux-test.yml"
}
```

**Output:**
```
<file>
00001| name: linux-test
00002| 
00003| on:
00004|   workflow_call:
00005|     inputs:
00006|       build-environment:
00007|         required: true
00008|         type: string
00009|         description: Top-level label for what's being built/tested.
00010|       test-matrix:
00011|         required: true
00012|         type: string
00013|         description: JSON description of what test configs to run.
00014|       docker-image:
00015|         required: true
00016|         type: string
00017|         description: Docker image to run in.
00018|       sync-tag:
00019|         required: false
00020|         type: string
00021|         default: ""
00022|         description: |
00023|           If this is set, our linter will use this to make sure that every other
00024|           job with the same `sync-tag` is identical.
00025|       timeout-minutes:
00026|         required: false
00027|         type: number
00028|         default: 240
00029|         description: |
00030|           Set the maximum (in minutes) how long the workflow should take to finish
00031|       use-gha:
00032|         required: false
00033|         type: string
00034|         default: ""
00035|         description: If set to any value, upload to GHA. Otherwise upload to S3.
00036|       dashboard-tag:
00037|         required: false
00038|         type: string
00039|         default: ""
00040|       s3-bucket:
00041|         description: S3 bucket to download artifact
00042|         required: false
00043|         type: string
00044|         default: "gha-artifacts"
00045|       aws-role-to-assume:
00046|         description: role to assume for downloading artifacts
00047|         required: false
00048|         type: string
00049|         default: ""
00050|       disable-monitor:
00051|         description: |
00052|           [Experimental] Disable utilization monitoring for tests.
00053|           Currently, by default we disable the monitor job and only look for specific tests,
00054|           since we are investigating the behaviour of the monitor script with different tests.
00055|         required: false
00056|         type: boolean
00057|         default: false
00058|     secrets:
00059|       HUGGING_FACE_HUB_TOKEN:
00060|         required: false
00061|         description: |
00062|           HF Auth token to avoid rate limits when downloading models or datasets from hub
00063|       SCRIBE_GRAPHQL_ACCESS_TOKEN:
00064|         required: false
00065|         description: |
00066|           FB app token to write to scribe endpoint
00067| 
00068| env:
00069|   GIT_DEFAULT_BRANCH: ${{ github.event.repository.default_branch }}
00070| 
00071| jobs:
00072|   test:
00073|     # Don't run on forked repos or empty test matrix
00074|     if: github.repository_owner == 'pytorch' && toJSON(fromJSON(inputs.test-matrix).include) != '[]'
00075|     strategy:
00076|       matrix: ${{ fromJSON(inputs.test-matrix) }}
00077|       fail-fast: false
00078|     environment: ${{ github.ref == 'refs/heads/main' && 'scribe-protected' || startsWith(github.ref, 'refs/heads/release/') && 'scribe-protected' || contains(github.event.pull_request.labels.*.name, 'ci-scribe') && 'scribe-pr' || '' }}
00079|     runs-on: ${{ matrix.runner }}
00080|     timeout-minutes: ${{ matrix.mem_leak_check == 'mem_leak_check' && 600 || inputs.timeout-minutes }}
00081|     steps:
00082|       - name: Setup SSH (Click me for login details)
00083|         uses: pytorch/test-infra/.github/actions/setup-ssh@release/2.6
00084|         if: ${{ !contains(matrix.runner, 'gcp.a100') }}
00085|         with:
00086|           github-secret: ${{ secrets.GITHUB_TOKEN }}
00087|           instructions: |
00088|             All testing is done inside the container, to start an interactive session run:
00089|               docker exec -it $(docker container ps --format '{{.ID}}') bash
00090| 
00091|       - name: Checkout PyTorch
00092|         uses: pytorch/pytorch/.github/actions/checkout-pytorch@release/2.6
00093|         with:
00094|           no-sudo: true
00095| 
00096|       - name: Setup Linux
00097|         uses: ./.github/actions/setup-linux
00098| 
00099|       - name: configure aws credentials
00100|         if : ${{ inputs.aws-role-to-assume != '' }}
00101|         uses: aws-actions/configure-aws-credentials@v3
00102|         with:
00103|           role-to-assume: ${{ inputs.aws-role-to-assume }}
00104|           role-session-name: gha-linux-test
00105|           aws-region: us-east-1
00106| 
00107|       - name: Calculate docker image
00108|         id: calculate-docker-image
00109|         uses: pytorch/test-infra/.github/actions/calculate-docker-image@release/2.6
00110|         with:
00111|           docker-image-name: ${{ inputs.docker-image }}
00112| 
00113|       - name: Use following to pull public copy of the image
00114|         id: print-ghcr-mirror
00115|         env:
00116|           ECR_DOCKER_IMAGE: ${{ steps.calculate-docker-image.outputs.docker-image }}
00117|         shell: bash
00118|         run: |
00119|           tag=${ECR_DOCKER_IMAGE##*/}
00120|           echo "docker pull ghcr.io/pytorch/ci-image:${tag/:/-}"
00121| 
00122|       - name: Pull docker image
00123|         uses: pytorch/test-infra/.github/actions/pull-docker-image@release/2.6
00124|         with:
00125|           docker-image: ${{ steps.calculate-docker-image.outputs.docker-image }}
00126| 
00127|       - name: Check if in a container runner
00128|         shell: bash
00129|         id: check_container_runner
00130|         run: echo "IN_CONTAINER_RUNNER=$(if [ -f /.inarc ] || [ -f /.incontainer ]; then echo true ; else echo false; fi)" >> "$GITHUB_OUTPUT"
00131| 
00132|       - name: Install nvidia driver, nvidia-docker runtime, set GPU_FLAG
00133|         id: install-nvidia-driver
00134|         uses: pytorch/test-infra/.github/actions/setup-nvidia@release/2.6
00135|         if: ${{ contains(inputs.build-environment, 'cuda') && !contains(matrix.config, 'nogpu') && steps.check_container_runner.outputs.IN_CONTAINER_RUNNER == 'false' }}
00136| 
00137|       - name: Setup GPU_FLAG for docker run
00138|         id: setup-gpu-flag
00139|         run: echo "GPU_FLAG=--gpus all -e NVIDIA_DRIVER_CAPABILITIES=all" >> "${GITHUB_ENV}"
00140|         if: ${{ contains(inputs.build-environment, 'cuda') && !contains(matrix.config, 'nogpu') && steps.check_container_runner.outputs.IN_CONTAINER_RUNNER == 'true' }}
00141| 
00142|       - name: Setup SCCACHE_SERVER_PORT environment for docker run when on container
00143|         id: setup-sscache-port-flag
00144|         run: echo "SCCACHE_SERVER_PORT_DOCKER_FLAG=-e SCCACHE_SERVER_PORT=$((RUNNER_UID + 4226))" >> "${GITHUB_ENV}"
00145|         if: ${{ steps.check_container_runner.outputs.IN_CONTAINER_RUNNER == 'true' }}
00146| 
00147|       - name: Lock NVIDIA A100 40GB Frequency
00148|         run: |
00149|           sudo nvidia-smi -pm 1
00150|           sudo nvidia-smi -ac 1215,1410
00151|           nvidia-smi
00152|         if: ${{ contains(matrix.runner, 'a100') && steps.check_container_runner.outputs.IN_CONTAINER_RUNNER == 'false' }}
00153| 
00154|       - name: Start monitoring script
00155|         id: monitor-script
00156|         if: ${{ !inputs.disable-monitor }}
00157|         shell: bash
00158|         continue-on-error: true
00159|         run: |
00160|           python3 -m pip install psutil==5.9.1 nvidia-ml-py==11.525.84
00161|           python3 -m tools.stats.monitor > usage_log.txt 2>&1 &
00162|           echo "monitor-script-pid=${!}" >> "${GITHUB_OUTPUT}"
00163| 
00164|       - name: Download build artifacts
00165|         uses: ./.github/actions/download-build-artifacts
00166|         with:
00167|           name: ${{ inputs.build-environment }}
00168|           s3-bucket: ${{ inputs.s3-bucket }}
00169| 
00170|       - name: Download TD artifacts
00171|         continue-on-error: true
00172|         uses: ./.github/actions/download-td-artifacts
00173| 
00174|       - name: Parse ref
00175|         id: parse-ref
00176|         run: .github/scripts/parse_ref.py
00177| 
00178|       - name: Get workflow job id
00179|         id: get-job-id
00180|         uses: ./.github/actions/get-workflow-job-id
00181|         if: always()
00182|         with:
00183|           github-token: ${{ secrets.GITHUB_TOKEN }}
00184| 
00185|       - name: Check for keep-going label and re-enabled test issues
00186|         # This uses the filter-test-configs action because it conviniently
00187|         # checks for labels and re-enabled test issues.  It does not actually do
00188|         # any filtering.  All filtering is done in the build step.
00189|         id: keep-going
00190|         uses: ./.github/actions/filter-test-configs
00191|         with:
00192|           github-token: ${{ secrets.GITHUB_TOKEN }}
00193|           test-matrix: ${{ inputs.test-matrix }}
00194|           job-name: ${{ steps.get-job-id.outputs.job-name }}
00195| 
00196|       - name: Set Test step time
00197|         id: test-timeout
00198|         shell: bash
00199|         env:
00200|           JOB_TIMEOUT: ${{ matrix.mem_leak_check == 'mem_leak_check' && 600 || inputs.timeout-minutes }}
00201|         run: |
00202|           echo "timeout=$((JOB_TIMEOUT-30))" >> "${GITHUB_OUTPUT}"
00203| 
00204|       - name: Test
00205|         id: test
00206|         timeout-minutes: ${{ fromJson(steps.test-timeout.outputs.timeout) }}
00207|         env:
00208|           BUILD_ENVIRONMENT: ${{ inputs.build-environment }}
00209|           PR_NUMBER: ${{ github.event.pull_request.number }}
00210|           GITHUB_REPOSITORY: ${{ github.repository }}
00211|           GITHUB_WORKFLOW: ${{ github.workflow }}
00212|           GITHUB_JOB: ${{ github.job }}
00213|           GITHUB_RUN_ID: ${{ github.run_id }}
00214|           GITHUB_RUN_NUMBER: ${{ github.run_number }}
00215|           GITHUB_RUN_ATTEMPT: ${{ github.run_attempt }}
00216|           JOB_ID: ${{ steps.get-job-id.outputs.job-id }}
00217|           JOB_NAME: ${{ steps.get-job-id.outputs.job-name }}
00218|           BRANCH: ${{ steps.parse-ref.outputs.branch }}
00219|           SHA1: ${{ github.event.pull_request.head.sha || github.sha }}
00220|           BASE_SHA: ${{ github.event.pull_request.base.sha || github.sha }}
00221|           TEST_CONFIG: ${{ matrix.config }}
00222|           SHARD_NUMBER: ${{ matrix.shard }}
00223|           NUM_TEST_SHARDS: ${{ matrix.num_shards }}
00224|           REENABLED_ISSUES: ${{ steps.keep-going.outputs.reenabled-issues }}
00225|           CONTINUE_THROUGH_ERROR: ${{ steps.keep-going.outputs.keep-going }}
00226|           VERBOSE_TEST_LOGS: ${{ steps.keep-going.outputs.ci-verbose-test-logs }}
00227|           TEST_SHOWLOCALS: ${{ steps.keep-going.outputs.ci-test-showlocals }}
00228|           NO_TEST_TIMEOUT: ${{ steps.keep-going.outputs.ci-no-test-timeout }}
00229|           NO_TD: ${{ steps.keep-going.outputs.ci-no-td }}
00230|           TD_DISTRIBUTED: ${{ steps.keep-going.outputs.ci-td-distributed }}
00231|           SCCACHE_BUCKET: ossci-compiler-cache-circleci-v2
00232|           SCCACHE_REGION: us-east-1
00233|           SCCACHE_S3_KEY_PREFIX: ${{ github.workflow }}
00234|           SHM_SIZE: ${{ contains(inputs.build-environment, 'cuda') && '2g' || '1g' }}
00235|           DOCKER_IMAGE: ${{ inputs.docker-image }}
00236|           XLA_CUDA: ${{ contains(inputs.build-environment, 'xla') && '0' || '' }}
00237|           XLA_CLANG_CACHE_S3_BUCKET_NAME: ossci-compiler-clang-cache-circleci-xla
00238|           PYTORCH_TEST_CUDA_MEM_LEAK_CHECK: ${{ matrix.mem_leak_check && '1' || '0' }}
00239|           PYTORCH_TEST_RERUN_DISABLED_TESTS: ${{ matrix.rerun_disabled_tests && '1' || '0' }}
00240|           DASHBOARD_TAG: ${{ inputs.dashboard-tag }}
00241|           HUGGING_FACE_HUB_TOKEN: ${{ secrets.HUGGING_FACE_HUB_TOKEN }}
00242|           SCRIBE_GRAPHQL_ACCESS_TOKEN: ${{ secrets.SCRIBE_GRAPHQL_ACCESS_TOKEN }}
00243|           IS_A100_RUNNER: ${{ contains(matrix.runner, 'a100') && '1' || '0' }}
00244|           ARTIFACTS_FILE_SUFFIX: ${{ github.job }}-${{ matrix.config }}-${{ matrix.shard }}-${{ matrix.num_shards }}-${{ matrix.runner }}_${{ steps.get-job-id.outputs.job-id }}
00245|         run: |
00246|           set -x
00247| 
00248|           if [[ $TEST_CONFIG == 'multigpu' ]]; then
00249|             TEST_COMMAND=.ci/pytorch/multigpu-test.sh
00250|           elif [[ $BUILD_ENVIRONMENT == *onnx* ]]; then
00251|             TEST_COMMAND=.ci/onnx/test.sh
00252|           else
00253|             TEST_COMMAND=.ci/pytorch/test.sh
00254|           fi
00255| 
00256|           # detached container should get cleaned up by teardown_ec2_linux
00257|           # TODO: Stop building test binaries as part of the build phase
00258|           # Used for GPU_FLAG since that doesn't play nice
00259|           # shellcheck disable=SC2086,SC2090
00260|           container_name=$(docker run \
00261|             ${GPU_FLAG:-} \
00262|             ${SCCACHE_SERVER_PORT_DOCKER_FLAG:-} \
00263|             -e BUILD_ENVIRONMENT \
00264|             -e PR_NUMBER \
00265|             -e GITHUB_ACTIONS \
00266|             -e GITHUB_REPOSITORY \
00267|             -e GITHUB_WORKFLOW \
00268|             -e GITHUB_JOB \
00269|             -e GITHUB_RUN_ID \
00270|             -e GITHUB_RUN_NUMBER \
00271|             -e GITHUB_RUN_ATTEMPT \
00272|             -e JOB_ID \
00273|             -e JOB_NAME \
00274|             -e BASE_SHA \
00275|             -e BRANCH \
00276|             -e SHA1 \
00277|             -e AWS_DEFAULT_REGION \
00278|             -e IN_WHEEL_TEST \
00279|             -e SHARD_NUMBER \
00280|             -e TEST_CONFIG \
00281|             -e NUM_TEST_SHARDS \
00282|             -e REENABLED_ISSUES \
00283|             -e CONTINUE_THROUGH_ERROR \
00284|             -e VERBOSE_TEST_LOGS \
00285|             -e TEST_SHOWLOCALS \
00286|             -e NO_TEST_TIMEOUT \
00287|             -e NO_TD \
00288|             -e TD_DISTRIBUTED \
00289|             -e PR_LABELS \
00290|             -e MAX_JOBS="$(nproc --ignore=2)" \
00291|             -e SCCACHE_BUCKET \
00292|             -e SCCACHE_REGION \
00293|             -e SCCACHE_S3_KEY_PREFIX \
00294|             -e XLA_CUDA \
00295|             -e XLA_CLANG_CACHE_S3_BUCKET_NAME \
00296|             -e PYTORCH_TEST_CUDA_MEM_LEAK_CHECK \
00297|             -e PYTORCH_TEST_RERUN_DISABLED_TESTS \
00298|             -e SKIP_SCCACHE_INITIALIZATION=1 \
00299|             -e HUGGING_FACE_HUB_TOKEN \
00300|             -e SCRIBE_GRAPHQL_ACCESS_TOKEN \
00301|             -e DASHBOARD_TAG \
00302|             -e IS_A100_RUNNER \
00303|             -e ARTIFACTS_FILE_SUFFIX \
00304|             --env-file="/tmp/github_env_${GITHUB_RUN_ID}" \
00305|             --security-opt seccomp=unconfined \
00306|             --cap-add=SYS_PTRACE \
00307|             --ipc=host \
00308|             --shm-size="${SHM_SIZE}" \
00309|             --tty \
00310|             --detach \
00311|             --name="${container_name}" \
00312|             --user jenkins \
00313|             -v "${GITHUB_WORKSPACE}:/var/lib/jenkins/workspace" \
00314|             -w /var/lib/jenkins/workspace \
00315|             "${DOCKER_IMAGE}"
00316|           )
00317|           # Propagate download.pytorch.org IP to container
00318|           grep download.pytorch.org /etc/hosts | docker exec -i "${container_name}" sudo bash -c "/bin/cat >> /etc/hosts"
00319|           echo "DOCKER_CONTAINER_ID=${container_name}" >> "${GITHUB_ENV}"
00320|           docker exec -t "${container_name}" sh -c "python3 -m pip install $(echo dist/*.whl)[opt-einsum] && ${TEST_COMMAND}"
00321| 
00322|       - name: Upload pytest cache if tests failed
00323|         uses: ./.github/actions/pytest-cache-upload
00324|         continue-on-error: true
00325|         if: failure() && steps.test.conclusion && steps.test.conclusion == 'failure'
00326|         with:
00327|           cache_dir: .pytest_cache
00328|           shard: ${{ matrix.shard }}
00329|           sha: ${{ github.event.pull_request.head.sha || github.sha }}
00330|           test_config: ${{ matrix.config }}
00331|           job_identifier: ${{ github.workflow }}_${{ inputs.build-environment }}
00332| 
00333|       - name: Upload the benchmark results
00334|         uses: pytorch/test-infra/.github/actions/upload-benchmark-results@release/2.6
00335|         with:
00336|           benchmark-results-dir: test/test-reports
00337|           dry-run: false
00338|           schema-version: v3
00339|           github-token: ${{ secrets.GITHUB_TOKEN }}
00340| 
00341|       - name: Print remaining test logs
00342|         shell: bash
00343|         if: always() && steps.test.conclusion
00344|         run: |
00345|           cat test/**/*_toprint.log || true
00346| 
00347|       - name: Stop monitoring script
00348|         if: ${{ always() && steps.monitor-script.outputs.monitor-script-pid }}
00349|         shell: bash
00350|         continue-on-error: true
00351|         env:
00352|           MONITOR_SCRIPT_PID: ${{ steps.monitor-script.outputs.monitor-script-pid }}
00353|         run: |
00354|           kill "$MONITOR_SCRIPT_PID"
00355| 
00356|       - name: Upload test artifacts
00357|         uses: ./.github/actions/upload-test-artifacts
00358|         if: always() && steps.test.conclusion && steps.test.conclusion != 'skipped'
00359|         with:
00360|           file-suffix: ${{ github.job }}-${{ matrix.config }}-${{ matrix.shard }}-${{ matrix.num_shards }}-${{ matrix.runner }}_${{ steps.get-job-id.outputs.job-id }}
00361|           use-gha: ${{ inputs.use-gha }}
00362|           s3-bucket: ${{ inputs.s3-bucket }}
00363| 
00364|       - name: Collect backtraces from coredumps (if any)
00365|         if: always()
00366|         run: |
00367|           # shellcheck disable=SC2156
00368|           find . -iname "core.[1-9]*" -exec docker exec "${DOCKER_CONTAINER_ID}" sh -c "gdb python {} -ex 'bt' -ex 'q'" \;
00369| 
00370|       - name: Store Core dumps on S3
00371|         uses: seemethere/upload-artifact-s3@v5
00372|         if: failure()
00373|         with:
00374|           name: coredumps-${{ matrix.config }}-${{ matrix.shard }}-${{ matrix.num_shards }}-${{ matrix.runner }}
00375|           retention-days: 14
00376|           if-no-files-found: ignore
00377|           path: ./**/core.[1-9]*
00378| 
00379|       - name: Teardown Linux
00380|         uses: pytorch/test-infra/.github/actions/teardown-linux@release/2.6
00381|         if: always() && steps.check_container_runner.outputs.IN_CONTAINER_RUNNER == 'false'
00382| 
00383|       # NB: We are currently having an intermittent GPU-related issue on G5 runners with
00384|       # A10G GPU. Once this happens, trying to reset the GPU as done in setup-nvidia does
00385|       # not seem to help. Here are some symptoms:
00386|       #   * Calling nvidia-smi timeouts after 60 second
00387|       #   * Fail to run nvidia-smi with an unable to determine the device handle for GPU
00388|       #     unknown error
00389|       #   * Test fails with a missing CUDA GPU error when initializing CUDA in PyTorch
00390|       #   * Run docker --gpus all fails with error response from daemon
00391|       #
00392|       # As both the root cause and recovery path are unclear, let's take the runner out of
00393|       # service so that it doesn't get any more jobs
00394|       - name: Check NVIDIA driver installation step
00395|         if: failure() && steps.install-nvidia-driver.outcome && steps.install-nvidia-driver.outcome != 'skipped'
00396|         shell: bash
00397|         env:
00398|           RUNNER_WORKSPACE: ${{ runner.workspace }}
00399|         run: |
00400|           set +e
00401|           set -x
00402| 
00403|           nvidia-smi
00404|           # NB: Surprisingly, nvidia-smi command returns successfully with return code 0 even in
00405|           # the case where the driver has already crashed as it still can get the driver version
00406|           # and some basic information like the bus ID.  However, the rest of the information
00407|           # would be missing (ERR!), for example:
00408|           #
00409|           # +-----------------------------------------------------------------------------+
00410|           # | NVIDIA-SMI 525.89.02    Driver Version: 525.89.02    CUDA Version: 12.0     |
00411|           # |-------------------------------+----------------------+----------------------+
00412|           # | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
00413|           # | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
00414|           # |                               |                      |               MIG M. |
00415|           # |===============================+======================+======================|
00416|           # |   0  ERR!                Off  | 00000000:00:1E.0 Off |                 ERR! |
00417|           # |ERR!  ERR! ERR!    ERR! / ERR! |   4184MiB / 23028MiB |    ERR!      Default |
00418|           # |                               |                      |                 ERR! |
00419|           # +-------------------------------+----------------------+----------------------+
00420|           #
00421|           # +-----------------------------------------------------------------------------+
00422|           # | Processes:                                                                  |
00423|           # |  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
00424|           # |        ID   ID                                                   Usage      |
00425|           # |=============================================================================|
00426|           # +-----------------------------------------------------------------------------+
00427|           #
00428|           # This should be reported as a failure instead as it will guarantee to fail when
00429|           # Docker tries to run with --gpus all
00430|           #
00431|           # So, the correct check here is to query one of the missing piece of info like
00432|           # GPU name, so that the command can fail accordingly
00433|           nvidia-smi --query-gpu=gpu_name --format=csv,noheader --id=0
00434|           NVIDIA_SMI_STATUS=$?
00435| 
00436|           # These are acceptable return code from nvidia-smi as copied from setup-nvidia GitHub action
00437|           if [ "$NVIDIA_SMI_STATUS" -ne 0 ] && [ "$NVIDIA_SMI_STATUS" -ne 14 ]; then
00438|             echo "NVIDIA driver installation has failed, shutting down the runner..."
00439|             .github/scripts/stop_runner_service.sh
00440|           fi
00441| 
00442|           # For runner with multiple GPUs, we also want to confirm that the number of GPUs are the
00443|           # power of 2, i.e. 1, 2, 4, or 8. This is to avoid flaky test issue when one GPU fails
00444|           # https://github.com/pytorch/test-infra/issues/4000
00445|           GPU_COUNT=$(nvidia-smi --list-gpus | wc -l)
00446|           NVIDIA_SMI_STATUS=$?
00447| 
00448|           # These are acceptable return code from nvidia-smi as copied from setup-nvidia GitHub action
00449|           if [ "$NVIDIA_SMI_STATUS" -ne 0 ] && [ "$NVIDIA_SMI_STATUS" -ne 14 ]; then
00450|             echo "NVIDIA driver installation has failed, shutting down the runner..."
00451|             .github/scripts/stop_runner_service.sh
00452|           fi
00453| 
00454|           # Check the GPU count to be a power of 2
00455|           if [ "$GPU_COUNT" -le 8 ] && [ "$GPU_COUNT" -ne 1 ] && [ "$GPU_COUNT" -ne 2 ] && [ "$GPU_COUNT" -ne 4 ] && [ "$GPU_COUNT" -ne 8 ]; then
00456|             echo "NVIDIA driver detects $GPU_COUNT GPUs. The runner has a broken GPU, shutting it down..."
00457|             .github/scripts/stop_runner_service.sh
00458|           fi
00459| 

(End of file - total 459 lines)
</file>
```

**Tool: bash**

**Input:**
```json
{
  "command": "ls -la .github/templates",
  "description": "List templates directory",
  "workdir": "D:\\oss\\opensource\\pytorch-2.6.0"
}
```

**Output:**
```
total 44
drwxr-xr-x 1 liutuo 197121    0 Nov 13 16:48 .
drwxr-xr-x 1 liutuo 197121    0 Nov 13 16:48 ..
-rw-r--r-- 1 liutuo 197121 5960 Jan 29  2025 common.yml.j2
-rw-r--r-- 1 liutuo 197121 7202 Jan 29  2025 linux_binary_build_workflow.yml.j2
-rw-r--r-- 1 liutuo 197121 4949 Jan 29  2025 macos_binary_build_workflow.yml.j2
-rw-r--r-- 1 liutuo 197121 2869 Jan 29  2025 upload.yml.j2
-rw-r--r-- 1 liutuo 197121 5382 Jan 29  2025 windows_binary_build_workflow.yml.j2

```

---

## Assistant (Build · openrouter/pony-alpha · 28.6s)

_Thinking:_

Let me also look at some more workflows and scripts to understand the full architecture. I should look at the lint workflow, the inductor workflow, the periodic workflow, and the actions directory.

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\lint.yml"
}
```

**Output:**
```
<file>
00001| name: Lint
00002| 
00003| on:
00004|   pull_request:
00005|     branches-ignore:
00006|       - nightly
00007|   push:
00008|     branches:
00009|       - main
00010|       - release/*
00011|       - landchecks/*
00012|   workflow_dispatch:
00013| 
00014| permissions: read-all
00015| # The names of steps that actually test the code should be suffixed with `(nonretryable)`.
00016| # When any other step fails, it's job will be retried once by retryBot.
00017| jobs:
00018|   get-label-type:
00019|     if: github.repository_owner == 'pytorch'
00020|     name: get-label-type
00021|     uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
00022|     with:
00023|       triggering_actor: ${{ github.triggering_actor }}
00024|       issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
00025|       curr_branch: ${{ github.head_ref || github.ref_name }}
00026| 
00027|   lintrunner-clang:
00028|     uses: pytorch/test-infra/.github/workflows/linux_job.yml@release/2.6
00029|     needs: get-label-type
00030|     with:
00031|       timeout: 120
00032|       runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge"
00033|       docker-image: pytorch-linux-jammy-cuda11.8-cudnn9-py3.9-linter
00034|       # NB: A shallow checkout won't work here because calculate-docker-image requires a full checkout
00035|       # to run git rev-parse HEAD~:.ci/docker when a new image is needed
00036|       fetch-depth: 0
00037|       submodules: true
00038|       ref: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || github.sha }}
00039|       script: |
00040|         export ADDITIONAL_LINTRUNNER_ARGS="--take CLANGTIDY,CLANGFORMAT --all-files"
00041|         export CLANG=1
00042|         .github/scripts/lintrunner.sh
00043| 
00044|   lintrunner-noclang:
00045|     uses: pytorch/test-infra/.github/workflows/linux_job.yml@release/2.6
00046|     needs: get-label-type
00047|     with:
00048|       timeout: 120
00049|       runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge"
00050|       docker-image: pytorch-linux-jammy-cuda11.8-cudnn9-py3.9-linter
00051|       # NB: A shallow checkout won't work here because calculate-docker-image requires a full checkout
00052|       # to run git rev-parse HEAD~:.ci/docker when a new image is needed
00053|       fetch-depth: 0
00054|       submodules: true
00055|       ref: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || github.sha }}
00056|       script: |
00057|         export ADDITIONAL_LINTRUNNER_ARGS="--skip CLANGTIDY,CLANGFORMAT --all-files"
00058|         .github/scripts/lintrunner.sh
00059| 
00060|   quick-checks:
00061|     uses: pytorch/test-infra/.github/workflows/linux_job.yml@release/2.6
00062|     needs: get-label-type
00063|     with:
00064|       timeout: 120
00065|       runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge"
00066|       docker-image: pytorch-linux-focal-linter
00067|       fetch-depth: 0
00068|       ref: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || github.sha }}
00069|       script: |
00070|         # The generic Linux job chooses to use base env, not the one setup by the image
00071|         CONDA_ENV=$(conda env list --json | jq -r ".envs | .[-1]")
00072|         conda activate "${CONDA_ENV}"
00073| 
00074|         # Ensure no non-breaking spaces
00075|         # NB: We use 'printf' below rather than '\u000a' since bash pre-4.2
00076|         # does not support the '\u000a' syntax (which is relevant for local linters)
00077|         (! git --no-pager grep -In "$(printf '\xC2\xA0')" -- . || (echo "The above lines have non-breaking spaces (U+00A0); please convert them to spaces (U+0020)"; false))
00078| 
00079|         # Ensure cross-OS compatible file names
00080|         (! git ls-files | grep -E '([<>:"|?*]|[ .]$)' || (echo "The above file names are not valid across all operating systems. Please ensure they don't contain the characters '<>:""|?*' and don't end with a white space or a '.' "; false))
00081| 
00082|         # Ensure no versionless Python shebangs
00083|         (! git --no-pager grep -In '#!.*python$' -- . || (echo "The above lines have versionless Python shebangs; please specify either python2 or python3"; false))
00084| 
00085|         # Ensure ciflow tags mentioned in config
00086|         python3 .github/scripts/collect_ciflow_labels.py --validate-tags
00087| 
00088|         # C++ docs check
00089|         pushd docs/cpp/source
00090|         ./check-doxygen.sh
00091|         popd
00092| 
00093|         # CUDA kernel launch check
00094|         set -eux
00095|         python3 torch/testing/_internal/check_kernel_launches.py |& tee cuda_kernel_launch_checks.txt
00096| 
00097|   pr-sanity-checks:
00098|     name: pr-sanity-checks
00099|     needs: get-label-type
00100|     runs-on: [self-hosted, "${{ needs.get-label-type.outputs.label-type }}linux.large"]
00101|     # Only run this on pull requests. This check is simple enough to be done without a Docker image
00102|     if: github.event_name == 'pull_request' && !contains(github.event.pull_request.labels.*.name, 'skip-pr-sanity-checks')
00103|     steps:
00104|       - name: Checkout PyTorch
00105|         uses: pytorch/pytorch/.github/actions/checkout-pytorch@release/2.6
00106|         with:
00107|           submodules: false
00108|           fetch-depth: -1
00109| 
00110|       - name: PR size check (nonretryable)
00111|         env:
00112|           BASE: ${{ github.event.pull_request.base.sha }}
00113|           HEAD: ${{ github.event.pull_request.head.sha }}
00114|         run: |
00115|           bash .github/scripts/pr-sanity-check.sh
00116| 
00117|   workflow-checks:
00118|     uses: pytorch/test-infra/.github/workflows/linux_job.yml@release/2.6
00119|     needs: get-label-type
00120|     with:
00121|       timeout: 120
00122|       runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge"
00123|       docker-image: pytorch-linux-focal-linter
00124|       fetch-depth: -1
00125|       submodules: true
00126|       ref: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || github.sha }}
00127|       script: |
00128|         # The generic Linux job chooses to use base env, not the one setup by the image
00129|         CONDA_ENV=$(conda env list --json | jq -r ".envs | .[-1]")
00130|         conda activate "${CONDA_ENV}"
00131| 
00132|         # Regenerate workflows
00133|         export RELEASE_VERSION_TAG=2.6
00134|         .github/scripts/generate_ci_workflows.py
00135| 
00136|         RC=0
00137|         # Assert that regenerating the workflows didn't change them
00138|         if ! .github/scripts/report_git_status.sh .github/workflows; then
00139|           echo
00140|           echo 'As shown by the above diff, the committed .github/workflows'
00141|           echo 'are not up to date according to .github/templates.'
00142|           echo 'Please run this command, commit, and push again to your PR:'
00143|           echo
00144|           echo '    .github/scripts/generate_ci_workflows.py'
00145|           echo
00146|           echo 'If running that command does nothing, you may need to rebase'
00147|           echo 'onto a more recent commit from the PyTorch main branch.'
00148|           RC=1
00149|         fi
00150| 
00151|         # Check that jobs will be cancelled
00152|         .github/scripts/ensure_actions_will_cancel.py
00153| 
00154|         exit $RC
00155| 
00156|   toc:
00157|     uses: pytorch/test-infra/.github/workflows/linux_job.yml@release/2.6
00158|     needs: get-label-type
00159|     with:
00160|       timeout: 120
00161|       runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge"
00162|       docker-image: pytorch-linux-focal-linter
00163|       fetch-depth: 0
00164|       ref: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || github.sha }}
00165|       script: |
00166|         # The generic Linux job chooses to use base env, not the one setup by the image
00167|         CONDA_ENV=$(conda env list --json | jq -r ".envs | .[-1]")
00168|         conda activate "${CONDA_ENV}"
00169| 
00170|         # Regenerate ToCs and check that they didn't change
00171|         set -eu
00172| 
00173|         export PATH=~/.npm-global/bin:"$PATH"
00174|         for FILE in $(git grep -Il '<!-- toc -->' -- '**.md'); do
00175|           markdown-toc --bullets='-' -i "$FILE"
00176|         done
00177| 
00178|         if ! .github/scripts/report_git_status.sh .; then
00179|           echo
00180|           echo 'As shown by the above diff, the table of contents in one or'
00181|           echo 'more Markdown files is not up to date with the file contents.'
00182|           echo 'You can either apply that Git diff directly to correct the'
00183|           echo 'table of contents, or if you have npm installed, you can'
00184|           echo 'install the npm package markdown-toc and run the following'
00185|           # shellcheck disable=SC2016
00186|           echo 'command (replacing $FILE with the filename for which you want'
00187|           echo 'to regenerate the table of contents):'
00188|           echo
00189|           # shellcheck disable=SC2016
00190|           echo "    markdown-toc --bullets='-' -i \"\$FILE\""
00191|           false
00192|         fi
00193| 
00194|   test-tools:
00195|     name: Test tools
00196|     if: ${{ github.repository == 'pytorch/pytorch' }}
00197|     uses: pytorch/test-infra/.github/workflows/linux_job.yml@release/2.6
00198|     needs: get-label-type
00199|     with:
00200|       timeout: 120
00201|       runner: "${{ needs.get-label-type.outputs.label-type }}linux.2xlarge"
00202|       docker-image: pytorch-linux-focal-linter
00203|       fetch-depth: 0
00204|       ref: ${{ github.event_name == 'pull_request' && github.event.pull_request.head.sha || github.sha }}
00205|       script: |
00206|         # The generic Linux job chooses to use base env, not the one setup by the image
00207|         CONDA_ENV=$(conda env list --json | jq -r ".envs | .[-1]")
00208|         conda activate "${CONDA_ENV}"
00209| 
00210|         # Test tools
00211|         PYTHONPATH=$(pwd) pytest tools/test/test_*.py
00212|         PYTHONPATH=$(pwd) pytest .github/scripts/test_*.py
00213| 
00214|   test_run_test:
00215|     name: Test `run_test.py` is usable without boto3
00216|     if: ${{ github.repository == 'pytorch/pytorch' }}
00217|     runs-on: linux.20_04.4x
00218|     steps:
00219|       - name: Checkout PyTorch
00220|         uses: pytorch/pytorch/.github/actions/checkout-pytorch@release/2.6
00221|         with:
00222|           submodules: false
00223|           fetch-depth: 1
00224|       - name: Setup Python 3.9
00225|         uses: actions/setup-python@v4
00226|         with:
00227|           python-version: '3.9'
00228|           architecture: x64
00229|           cache: pip
00230|       - name: Install dependencies
00231|         run: |
00232|           python3 -m pip install --upgrade pip
00233|           pip install pytest-rerunfailures==11.1.* pytest-flakefinder==1.1.* pytest-xdist==3.3.* expecttest==0.2.* fbscribelogger==0.1.* numpy==1.24.*
00234|           pip install torch --pre --index-url https://download.pytorch.org/whl/nightly/cpu/
00235|       - name: Run run_test.py (nonretryable)
00236|         run: |
00237|           # Run test_vulkan, which is a fast noop on Linux
00238|           python3 test/run_test.py --include test_vulkan --verbose
00239| 
00240|   test_collect_env:
00241|     if: ${{ github.repository == 'pytorch/pytorch' }}
00242|     name: Test collect_env
00243|     runs-on: linux.20_04.4x
00244|     strategy:
00245|       matrix:
00246|         test_type: [with_torch, without_torch, older_python_version]
00247|     steps:
00248|       # [see note: pytorch repo ref]
00249|       # deep clone (fetch-depth 0) required, to allow us to use git log
00250|       - name: Checkout PyTorch
00251|         uses: pytorch/pytorch/.github/actions/checkout-pytorch@release/2.6
00252|         with:
00253|           submodules: false
00254|           fetch-depth: 1
00255|       - name: Setup Python 3.6
00256|         if: matrix.test_type == 'older_python_version'
00257|         uses: actions/setup-python@v4
00258|         with:
00259|           python-version: '3.6'
00260|           architecture: x64
00261|           check-latest: false
00262|           cache: pip
00263|           cache-dependency-path: |
00264|             **/requirements.txt
00265|       - name: Setup Python 3.9
00266|         if: matrix.test_type != 'older_python_version'
00267|         uses: actions/setup-python@v4
00268|         with:
00269|           python-version: '3.9'
00270|           architecture: x64
00271|           check-latest: false
00272|           cache: pip
00273|           cache-dependency-path: |
00274|             **/requirements.txt
00275|       - name: Install torch
00276|         if: matrix.test_type == 'with_torch'
00277|         run: |
00278|           pip install -r requirements.txt
00279|           # Doesn't really matter what torch version, we just need ANY torch installed
00280|           pip install 'torch==2.*'
00281|       - name: Run collect_env.py (nonretryable)
00282|         run: |
00283|           # All we need to see is that it passes
00284|           python3 torch/utils/collect_env.py
00285| 
00286| concurrency:
00287|   group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.sha }}-${{ github.event_name == 'workflow_dispatch' }}
00288|   cancel-in-progress: true
00289| 

(End of file - total 289 lines)
</file>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\periodic.yml"
}
```

**Output:**
```
<file>
00001| name: periodic
00002| 
00003| on:
00004|   schedule:
00005|     # We have several schedules so jobs can check github.event.schedule to activate only for a fraction of the runs.
00006|     # Also run less frequently on weekends.
00007|     - cron: 45 0,8,16 * * 1-5
00008|     - cron: 45 4 * * 0,6
00009|     - cron: 45 4,12,20 * * 1-5
00010|     - cron: 45 12 * * 0,6
00011|     - cron: 29 8 * * *  # about 1:29am PDT, for mem leak check and rerun disabled tests
00012|   push:
00013|     tags:
00014|       - ciflow/periodic/*
00015|     branches:
00016|       - release/*
00017|   workflow_dispatch:
00018| 
00019| concurrency:
00020|   group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref_name }}-${{ github.ref_type == 'branch' && github.sha }}-${{ github.event_name == 'workflow_dispatch' }}-${{ github.event_name == 'schedule' }}-${{ github.event.schedule }}
00021|   cancel-in-progress: true
00022| 
00023| permissions: read-all
00024| 
00025| jobs:
00026|   llm-td:
00027|     if: github.repository_owner == 'pytorch'
00028|     name: before-test
00029|     uses: ./.github/workflows/llm_td_retrieval.yml
00030|     permissions:
00031|       id-token: write
00032|       contents: read
00033| 
00034|   target-determination:
00035|     name: before-test
00036|     uses: ./.github/workflows/target_determination.yml
00037|     needs: llm-td
00038|     permissions:
00039|       id-token: write
00040|       contents: read
00041| 
00042|   get-label-type:
00043|     name: get-label-type
00044|     uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
00045|     if: (github.event_name != 'schedule' || github.repository == 'pytorch/pytorch') && github.repository_owner == 'pytorch'
00046|     with:
00047|       triggering_actor: ${{ github.triggering_actor }}
00048|       issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
00049|       curr_branch: ${{ github.head_ref || github.ref_name }}
00050|       curr_ref_type: ${{ github.ref_type }}
00051| 
00052|   linux-focal-cuda12_1-py3_10-gcc9-build:
00053|     name: linux-focal-cuda12.1-py3.10-gcc9
00054|     uses: ./.github/workflows/_linux-build.yml
00055|     needs: get-label-type
00056|     with:
00057|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00058|       build-environment: linux-focal-cuda12.1-py3.10-gcc9
00059|       docker-image-name: pytorch-linux-focal-cuda12.1-cudnn9-py3-gcc9
00060|       test-matrix: |
00061|         { include: [
00062|           { config: "nogpu_AVX512", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00063|           { config: "nogpu_AVX512", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00064|           { config: "nogpu_NO_AVX2", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00065|           { config: "nogpu_NO_AVX2", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00066|           { config: "jit_legacy", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00067|         ]}
00068|     secrets: inherit
00069| 
00070|   linux-focal-cuda12_1-py3_10-gcc9-test:
00071|     name: linux-focal-cuda12.1-py3.10-gcc9
00072|     uses: ./.github/workflows/_linux-test.yml
00073|     needs:
00074|       - linux-focal-cuda12_1-py3_10-gcc9-build
00075|       - target-determination
00076|     with:
00077|       build-environment: linux-focal-cuda12.1-py3.10-gcc9
00078|       docker-image: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-build.outputs.docker-image }}
00079|       test-matrix: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-build.outputs.test-matrix }}
00080|     secrets: inherit
00081| 
00082|   linux-focal-cuda12_4-py3_10-gcc9-build:
00083|     name: linux-focal-cuda12.4-py3.10-gcc9
00084|     uses: ./.github/workflows/_linux-build.yml
00085|     needs: get-label-type
00086|     with:
00087|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00088|       build-environment: linux-focal-cuda12.4-py3.10-gcc9
00089|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9
00090|       test-matrix: |
00091|         { include: [
00092|           { config: "default", shard: 1, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00093|           { config: "default", shard: 2, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00094|           { config: "default", shard: 3, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00095|           { config: "default", shard: 4, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00096|           { config: "default", shard: 5, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00097|           { config: "nogpu_AVX512", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00098|           { config: "nogpu_AVX512", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00099|           { config: "nogpu_NO_AVX2", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00100|           { config: "nogpu_NO_AVX2", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00101|           { config: "jit_legacy", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00102|         ]}
00103|     secrets: inherit
00104| 
00105|   linux-focal-cuda12_4-py3_10-gcc9-test:
00106|     name: linux-focal-cuda12.4-py3.10-gcc9
00107|     uses: ./.github/workflows/_linux-test.yml
00108|     needs:
00109|       - linux-focal-cuda12_4-py3_10-gcc9-build
00110|       - target-determination
00111|     with:
00112|       timeout-minutes: 360
00113|       build-environment: linux-focal-cuda12.4-py3.10-gcc9
00114|       docker-image: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-build.outputs.docker-image }}
00115|       test-matrix: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-build.outputs.test-matrix }}
00116|     secrets: inherit
00117| 
00118|   linux-focal-cuda11_8-py3_9-gcc9-build:
00119|     name: linux-focal-cuda11.8-py3.9-gcc9
00120|     uses: ./.github/workflows/_linux-build.yml
00121|     needs: get-label-type
00122|     with:
00123|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00124|       build-environment: linux-focal-cuda11.8-py3.9-gcc9
00125|       docker-image-name: pytorch-linux-focal-cuda11.8-cudnn9-py3-gcc9
00126|       cuda-arch-list: 8.6
00127|       test-matrix: |
00128|         { include: [
00129|           { config: "multigpu", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g5.12xlarge.nvidia.gpu", owners: ["oncall:distributed"] },
00130|         ]}
00131|       build-with-debug: false
00132|     secrets: inherit
00133| 
00134|   linux-focal-cuda11_8-py3_9-gcc9-test:
00135|     name: linux-focal-cuda11.8-py3.9-gcc9
00136|     uses: ./.github/workflows/_linux-test.yml
00137|     needs: linux-focal-cuda11_8-py3_9-gcc9-build
00138|     with:
00139|       build-environment: linux-focal-cuda11.8-py3.9-gcc9
00140|       docker-image: ${{ needs.linux-focal-cuda11_8-py3_9-gcc9-build.outputs.docker-image }}
00141|       test-matrix: ${{ needs.linux-focal-cuda11_8-py3_9-gcc9-build.outputs.test-matrix }}
00142|     secrets: inherit
00143| 
00144|   linux-focal-cuda11_8-py3_10-gcc9-debug-build:
00145|     name: linux-focal-cuda11.8-py3.10-gcc9-debug
00146|     uses: ./.github/workflows/_linux-build.yml
00147|     needs: get-label-type
00148|     with:
00149|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00150|       build-environment: linux-focal-cuda11.8-py3.10-gcc9-debug
00151|       docker-image-name: pytorch-linux-focal-cuda11.8-cudnn9-py3-gcc9
00152|       build-with-debug: true
00153|       test-matrix: |
00154|         { include: [
00155|           { config: "default", shard: 1, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu", owners: ["oncall:debug-build"] },
00156|           { config: "default", shard: 2, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu", owners: ["oncall:debug-build"] },
00157|           { config: "default", shard: 3, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu", owners: ["oncall:debug-build"] },
00158|           { config: "default", shard: 4, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu", owners: ["oncall:debug-build"] },
00159|           { config: "default", shard: 5, num_shards: 5, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu", owners: ["oncall:debug-build"] },
00160|         ]}
00161|     secrets: inherit
00162| 
00163|   linux-focal-cuda11_8-py3_10-gcc9-debug-test:
00164|     name: linux-focal-cuda11.8-py3.10-gcc9-debug
00165|     uses: ./.github/workflows/_linux-test.yml
00166|     needs:
00167|       - linux-focal-cuda11_8-py3_10-gcc9-debug-build
00168|       - target-determination
00169|     with:
00170|       build-environment: linux-focal-cuda11.8-py3.10-gcc9-debug
00171|       docker-image: ${{ needs.linux-focal-cuda11_8-py3_10-gcc9-debug-build.outputs.docker-image }}
00172|       test-matrix: ${{ needs.linux-focal-cuda11_8-py3_10-gcc9-debug-build.outputs.test-matrix }}
00173|     secrets: inherit
00174| 
00175|   linux-focal-rocm6_2-py3_10-build:
00176|     name: linux-focal-rocm6.2-py3.10
00177|     uses: ./.github/workflows/_linux-build.yml
00178|     needs: get-label-type
00179|     with:
00180|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00181|       build-environment: linux-focal-rocm6.2-py3.10
00182|       docker-image-name: pytorch-linux-focal-rocm-n-py3
00183|       test-matrix: |
00184|         { include: [
00185|           { config: "distributed", shard: 1, num_shards: 3, runner: "linux.rocm.gpu", owners: ["module:rocm", "oncall:distributed"] },
00186|           { config: "distributed", shard: 2, num_shards: 3, runner: "linux.rocm.gpu", owners: ["module:rocm", "oncall:distributed"] },
00187|           { config: "distributed", shard: 3, num_shards: 3, runner: "linux.rocm.gpu", owners: ["module:rocm", "oncall:distributed"] },
00188|         ]}
00189|     secrets: inherit
00190| 
00191|   linux-focal-rocm6_2-py3_10-test:
00192|     permissions:
00193|       id-token: write
00194|       contents: read
00195|     name: linux-focal-rocm6.2-py3.10
00196|     uses: ./.github/workflows/_rocm-test.yml
00197|     needs:
00198|       - linux-focal-rocm6_2-py3_10-build
00199|       - target-determination
00200|     with:
00201|       build-environment: linux-focal-rocm6.2-py3.10
00202|       docker-image: ${{ needs.linux-focal-rocm6_2-py3_10-build.outputs.docker-image }}
00203|       test-matrix: ${{ needs.linux-focal-rocm6_2-py3_10-build.outputs.test-matrix }}
00204|     secrets: inherit
00205| 
00206|   linux-focal-cuda12_1-py3_10-gcc9-experimental-split-build:
00207|     name: linux-focal-cuda12.1-py3.10-gcc9-experimental-split-build
00208|     uses: ./.github/workflows/_linux-build.yml
00209|     needs: get-label-type
00210|     if: false # See https://github.com/pytorch/pytorch/issues/138750
00211|     with:
00212|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00213|       use_split_build: true
00214|       build-environment: linux-focal-cuda12.1-py3.10-gcc9
00215|       docker-image-name: pytorch-linux-focal-cuda12.1-cudnn9-py3-gcc9
00216|       test-matrix: |
00217|         { include: [
00218|           { config: "nogpu_AVX512", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00219|           { config: "nogpu_AVX512", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00220|           { config: "nogpu_NO_AVX2", shard: 1, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00221|           { config: "nogpu_NO_AVX2", shard: 2, num_shards: 2, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge" },
00222|           { config: "jit_legacy", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00223|         ]}
00224|     secrets: inherit
00225| 
00226|   linux-focal-cuda12_1-py3_10-gcc9-experimental-split-build-test:
00227|     name: linux-focal-cuda12.1-py3.10-gcc9-experimental-split-build
00228|     uses: ./.github/workflows/_linux-test.yml
00229|     needs:
00230|       - linux-focal-cuda12_1-py3_10-gcc9-experimental-split-build
00231|       - target-determination
00232|     with:
00233|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-experimental-split-build
00234|       docker-image: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-experimental-split-build.outputs.docker-image }}
00235|       test-matrix: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-experimental-split-build.outputs.test-matrix }}
00236|     secrets: inherit
00237| 
00238| 
00239|   linux-focal-cuda11_8-py3_9-gcc9-experimental-split-build:
00240|     name: linux-focal-cuda11.8-py3.9-gcc9-experimental-split-build
00241|     uses: ./.github/workflows/_linux-build.yml
00242|     needs: get-label-type
00243|     if: false # See https://github.com/pytorch/pytorch/issues/138750
00244|     with:
00245|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00246|       use_split_build: true
00247|       build-environment: linux-focal-cuda11.8-py3.9-gcc9
00248|       docker-image-name: pytorch-linux-focal-cuda11.8-cudnn9-py3-gcc9
00249|       cuda-arch-list: 8.6
00250|       test-matrix: |
00251|         { include: [
00252|           { config: "multigpu", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g5.12xlarge.nvidia.gpu", owners: ["oncall:distributed"] },
00253|         ]}
00254|       build-with-debug: false
00255|     secrets: inherit
00256| 
00257|   linux-focal-cuda11_8-py3_9-gcc9-experimental-split-build-test:
00258|     name: linux-focal-cuda11.8-py3.9-gcc9-experimental-split-build-test
00259|     uses: ./.github/workflows/_linux-test.yml
00260|     needs:
00261|       - linux-focal-cuda11_8-py3_9-gcc9-experimental-split-build
00262|       - target-determination
00263|     with:
00264|       build-environment: linux-focal-cuda11.8-py3.9-gcc9-experimental-split-build
00265|       docker-image: ${{ needs.linux-focal-cuda11_8-py3_9-gcc9-experimental-split-build.outputs.docker-image }}
00266|       test-matrix: ${{ needs.linux-focal-cuda11_8-py3_9-gcc9-experimental-split-build.outputs.test-matrix }}
00267|     secrets: inherit
00268| 
00269|   linux-focal-cuda11_8-py3_10-gcc9-experimental-split-build:
00270|     name: linux-focal-cuda11.8-py3.10-gcc9-experimental-split-build
00271|     uses: ./.github/workflows/_linux-build.yml
00272|     needs: get-label-type
00273|     if: false # See https://github.com/pytorch/pytorch/issues/138750
00274|     with:
00275|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00276|       use_split_build: true
00277|       build-environment: linux-focal-cuda11.8-py3.10-gcc9
00278|       docker-image-name: pytorch-linux-focal-cuda11.8-cudnn9-py3-gcc9
00279|       cuda-arch-list: '7.5'
00280|       test-matrix: |
00281|         { include: [
00282|           { config: "distributed", shard: 1, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g4dn.12xlarge.nvidia.gpu", owners: ["oncall:distributed"] },
00283|           { config: "distributed", shard: 2, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g4dn.12xlarge.nvidia.gpu", owners: ["oncall:distributed"] },
00284|           { config: "distributed", shard: 3, num_shards: 3, runner: "${{ needs.get-label-type.outputs.label-type }}linux.g4dn.12xlarge.nvidia.gpu", owners: ["oncall:distributed"] },
00285|         ]}
00286|     secrets: inherit
00287| 
00288|   linux-focal-cuda11_8-py3_10-gcc9-experimental-split-build-test:
00289|     name: linux-focal-cuda11.8-py3.10-gcc9-experimental-split-build-test
00290|     uses: ./.github/workflows/_linux-test.yml
00291|     needs:
00292|       - linux-focal-cuda11_8-py3_10-gcc9-experimental-split-build
00293|       - target-determination
00294|     with:
00295|       timeout-minutes: 360
00296|       build-environment: linux-focal-cuda11.8-py3.10-gcc9-experimental-split-build
00297|       docker-image: ${{ needs.linux-focal-cuda11_8-py3_10-gcc9-experimental-split-build.outputs.docker-image }}
00298|       test-matrix: ${{ needs.linux-focal-cuda11_8-py3_10-gcc9-experimental-split-build.outputs.test-matrix }}
00299|     secrets: inherit
00300| 
00301|   linux-focal-cuda12_1-py3-gcc9-slow-gradcheck-build:
00302|     name: linux-focal-cuda12.1-py3-gcc9-slow-gradcheck
00303|     uses: ./.github/workflows/_linux-build.yml
00304|     needs: get-label-type
00305|     with:
00306|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00307|       build-environment: linux-focal-cuda12.1-py3-gcc9-slow-gradcheck
00308|       docker-image-name: pytorch-linux-focal-cuda12.1-cudnn9-py3-gcc9
00309|       cuda-arch-list: 8.6
00310|       test-matrix: |
00311|         { include: [
00312|           { config: "default", shard: 1, num_shards: 8, runner: "linux.g5.4xlarge.nvidia.gpu", owners: ["module:slowgradcheck"] },
00313|           { config: "default", shard: 2, num_shards: 8, runner: "linux.g5.4xlarge.nvidia.gpu", owners: ["module:slowgradcheck"] },
00314|           { config: "default", shard: 3, num_shards: 8, runner: "linux.g5.4xlarge.nvidia.gpu", owners: ["module:slowgradcheck"] },
00315|           { config: "default", shard: 4, num_shards: 8, runner: "linux.g5.4xlarge.nvidia.gpu", owners: ["module:slowgradcheck"] },
00316|           { config: "default", shard: 5, num_shards: 8, runner: "linux.g5.4xlarge.nvidia.gpu", owners: ["module:slowgradcheck"] },
00317|           { config: "default", shard: 6, num_shards: 8, runner: "linux.g5.4xlarge.nvidia.gpu", owners: ["module:slowgradcheck"] },
00318|           { config: "default", shard: 7, num_shards: 8, runner: "linux.g5.4xlarge.nvidia.gpu", owners: ["module:slowgradcheck"] },
00319|           { config: "default", shard: 8, num_shards: 8, runner: "linux.g5.4xlarge.nvidia.gpu", owners: ["module:slowgradcheck"] },
00320|         ]}
00321|     secrets: inherit
00322| 
00323|   linux-focal-cuda12_1-py3-gcc9-slow-gradcheck-test:
00324|     name: linux-focal-cuda12.1-py3-gcc9-slow-gradcheck
00325|     uses: ./.github/workflows/_linux-test.yml
00326|     needs:
00327|       - linux-focal-cuda12_1-py3-gcc9-slow-gradcheck-build
00328|       - target-determination
00329|     with:
00330|       build-environment: linux-focal-cuda12.1-py3-gcc9-slow-gradcheck
00331|       docker-image: ${{ needs.linux-focal-cuda12_1-py3-gcc9-slow-gradcheck-build.outputs.docker-image }}
00332|       test-matrix: ${{ needs.linux-focal-cuda12_1-py3-gcc9-slow-gradcheck-build.outputs.test-matrix }}
00333|       timeout-minutes: 300
00334|     secrets: inherit
00335| 
00336|   linux-focal-cuda12_4-py3_10-gcc9-bazel-test:
00337|     name: linux-focal-cuda12.4-py3.10-gcc9-bazel-test
00338|     uses: ./.github/workflows/_bazel-build-test.yml
00339|     needs: get-label-type
00340|     with:
00341|       runner: "${{ needs.get-label-type.outputs.label-type }}linux.large"
00342|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-bazel-test
00343|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9
00344|       cuda-version: "12.4"
00345|       test-matrix: |
00346|         { include: [
00347|           { config: "default", shard: 1, num_shards: 1, runner: "${{ needs.get-label-type.outputs.label-type }}linux.4xlarge.nvidia.gpu" },
00348|         ]}
00349|     secrets: inherit
00350| 

(End of file - total 350 lines)
</file>
```

**Tool: bash**

**Input:**
```json
{
  "command": "ls .github/actions/*/action.yml",
  "description": "List all action.yml files",
  "workdir": "D:\\oss\\opensource\\pytorch-2.6.0"
}
```

**Output:**
```
.github/actions/build-android/action.yml
.github/actions/checkout-pytorch/action.yml
.github/actions/chown-workspace/action.yml
.github/actions/diskspace-cleanup/action.yml
.github/actions/download-build-artifacts/action.yml
.github/actions/download-td-artifacts/action.yml
.github/actions/filter-test-configs/action.yml
.github/actions/get-workflow-job-id/action.yml
.github/actions/linux-test/action.yml
.github/actions/pytest-cache-download/action.yml
.github/actions/pytest-cache-upload/action.yml
.github/actions/setup-linux/action.yml
.github/actions/setup-rocm/action.yml
.github/actions/setup-win/action.yml
.github/actions/setup-xpu/action.yml
.github/actions/teardown-rocm/action.yml
.github/actions/teardown-win/action.yml
.github/actions/teardown-xpu/action.yml
.github/actions/test-pytorch-binary/action.yml
.github/actions/upload-sccache-stats/action.yml
.github/actions/upload-test-artifacts/action.yml

```

---

## Assistant (Build · openrouter/pony-alpha · 17.9s)

_Thinking:_

.
Now I have a good understanding of the CI architecture. Let me also check out the inductor workflow and the .ci directory to understand how tests are actually run.
Now I have a good understanding of the CI architecture. Let me also check out the inductor workflow and the .ci directory to understand how tests are actually run.
Now I have a good understanding of the CI architecture. Let me also check out the inductor workflow and the .ci directory to understand how tests are actually run.

**Tool: bash**

**Input:**
```json
{
  "command": "ls .ci",
  "description": "List .ci directory",
  "workdir": "D:\\oss\\opensource\\pytorch-2.6.0"
}
```

**Output:**
```
aarch64_linux
caffe2
docker
libtorch
magma
manywheel
onnx
pytorch
wheel

```

**Tool: bash**

**Input:**
```json
{
  "command": "ls .ci/pytorch",
  "description": "List .ci/pytorch directory",
  "workdir": "D:\\oss\\opensource\\pytorch-2.6.0"
}
```

**Output:**
```
README.md
build-mobile.sh
build.sh
check_binary.sh
codegen-test.sh
common-build.sh
common.sh
common_utils.sh
cpp_doc_push_script.sh
create_test_cert.py
docker-build-test.sh
docs-test.sh
fake_numpy
functorch_doc_push_script.sh
install_cache_xla.sh
macos-build-test.sh
macos-build.sh
macos-common.sh
macos-test.sh
multigpu-test.sh
perf_test
print_sccache_log.py
python_doc_push_script.sh
run_glootls_test.sh
run_tests.sh
short-perf-test-cpu.sh
short-perf-test-gpu.sh
smoke_test
test.sh
test_example_code
win-build.sh
win-test-helpers
win-test.sh
windows

```

---

## Assistant (Build · openrouter/pony-alpha · 102.6s)

_Thinking:_

.
Now I have enough information to provide a comprehensive analysis of the CI architecture. Let me create a clear diagram and explanation.
Now I have enough information to provide a comprehensive analysis of the CI architecture. Let me create a clear diagram and explanation.
Now I have enough information to provide a comprehensive analysis of the CI architecture. Let me create a clear diagram and explanation.

Based on my analysis, here's the **PyTorch CI/CD Architecture**:

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PYTORCH CI/CD ARCHITECTURE                           │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│                           TRIGGER SOURCES                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│  • pull_request (PRs to main, release/*)                                    │
│  • push (to main, release/*, landchecks/*)                                  │
│  • schedule (cron jobs)                                                      │
│  • workflow_dispatch (manual)                                               │
│  • tags (ciflow/trunk/*, ciflow/periodic/*)                                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      MAIN WORKFLOW TYPES                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌───────────────┐│
│  │   pull.yml  │    │  trunk.yml  │    │periodic.yml │    │   lint.yml    ││
│  │   (PR CI)   │    │ (Post-merge)│    │ (Scheduled) │    │   (Linting)   ││
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    └───────┬───────┘│
│         │                  │                  │                   │         │
└─────────┼──────────────────┼──────────────────┼───────────────────┼─────────┘
          │                  │                  │                   │
          ▼                  ▼                  ▼                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PRE-TEST PHASE (Reusable Workflows)                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────────────┐    ┌────────────────────────────────────────────┐│
│  │_runner-determinator │    │      llm_td_retrieval.yml                   ││
│  │.yml                  │    │   (LLM-based test target determination)     ││
│  │                      │    └──────────────────────┬─────────────────────┘│
│  │ Determines runner    │                           │                       │
│  │ type based on user   │                           ▼                       │
│  │ (oss/fb/try)         │    ┌────────────────────────────────────────────┐│
│  └──────────────────────┘    │      target_determination.yml              ││
│                              │   (Selects which tests to run based on     ││
│                              │    code changes)                           ││
│                              └────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    REUSABLE BUILD WORKFLOWS (_*-build.yml)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌───────────────────┐  ┌───────────────────┐  ┌──────────────────────────┐│
│  │  _linux-build.yml │  │   _mac-build.yml  │  │     _win-build.yml       ││
│  │                   │  │                   │  │                          ││
│  │ • Docker build    │  │ • macOS arm64     │  │ • Windows VS2019         ││
│  │ • GCC/Clang       │  │ • Python 3.9      │  │ • CPU/CUDA builds        ││
│  │ • CUDA/ROCm/XLA   │  │ • MPS support     │  │                          ││
│  └───────────────────┘  └───────────────────┘  └──────────────────────────┘│
│                                                                              │
│  ┌───────────────────┐  ┌───────────────────┐  ┌──────────────────────────┐│
│  │_binary-build-linux│  │ _bazel-build-test │  │      _docs.yml           ││
│  │.yml               │  │.yml               │  │                          ││
│  │                   │  │                   │  │                          ││
│  │ • Wheel builds    │  │ • Bazel testing   │  │ • Documentation builds   ││
│  │ • libtorch builds │  │                   │  │                          ││
│  └───────────────────┘  └───────────────────┘  └──────────────────────────┘│
│                                                                              │
│  OUTPUTS: docker-image, test-matrix (sharded test configs)                  │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    REUSABLE TEST WORKFLOWS (_*-test.yml)                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌───────────────────┐  ┌───────────────────┐  ┌──────────────────────────┐│
│  │  _linux-test.yml  │  │   _mac-test.yml   │  │     _win-test.yml        ││
│  │                   │  │                   │  │                          ││
│  │ • pytest sharded  │  │ • macOS testing   │  │ • Windows testing        ││
│  │ • Multiple configs│  │                   │  │                          ││
│  │   - default       │  └───────────────────┘  └──────────────────────────┘│
│  │   - distributed   │                                                    │
│  │   - jit_legacy    │  ┌───────────────────┐  ┌──────────────────────────┐│
│  │   - crossref      │  │  _rocm-test.yml   │  │     _xpu-test.yml        ││
│  │   - dynamo_wrapped│  │                   │  │                          ││
│  └───────────────────┘  │ • AMD GPU testing │  │ • Intel XPU testing      ││
│                         └───────────────────┘  └──────────────────────────┘│
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                      _mac-test-mps.yml                                │  │
│  │                    (Metal Performance Shaders testing)                │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COMPOSITE ACTIONS (.github/actions/)                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  Setup/Teardown:          Artifacts:              Testing:                  │
│  • setup-linux           • download-build-artifacts • linux-test           │
│  • setup-win             • upload-test-artifacts   • filter-test-configs   │
│  • setup-rocm            • download-td-artifacts   • pytest-cache-download │
│  • setup-xpu             • upload-sccache-stats    • pytest-cache-upload   │
│  • teardown-rocm                                   • test-pytorch-binary    │
│  • teardown-win          Utilities:                                        │
│  • teardown-xpu          • checkout-pytorch                                    │
│  • diskspace-cleanup     • get-workflow-job-id                                  │
│                           • chown-workspace                                      │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TEST EXECUTION (.ci/pytorch/)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐ │
│  │   build.sh   │  │   test.sh    │  │multigpu-test │  │docs-test.sh     │ │
│  │              │  │              │  │.sh           │  │                 │ │
│  │ Main build   │  │ Main test    │  │ Multi-GPU    │  │ Documentation   │ │
│  │ script       │  │ runner       │  │ tests        │  │ tests           │ │
│  └──────────────┘  └──────────────┘  └──────────────┘  └─────────────────┘ │
│                                                                              │
│  Test Configuration:                                                        │
│  • SHARD_NUMBER / NUM_TEST_SHARDS - Test sharding                          │
│  • TEST_CONFIG - Test type (default, distributed, jit_legacy, etc.)        │
│  • Build artifacts downloaded from S3                                       │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SPECIALIZED WORKFLOWS                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  INDUCTOR:                 DISTRIBUTED/PERFORMANCE:                          │
│  • inductor.yml           • torchbench.yml                                  │
│  • inductor-unittest.yml  • slow.yml                                        │
│  • inductor-rocm.yml      • target-determination-indexer.yml                │
│  • inductor-perf-test-*.yml                                                 │
│                                                                              │
│  BINARY BUILDS (Generated from templates):                                  │
│  • generated-linux-binary-manywheel-*.yml                                   │
│  • generated-linux-binary-libtorch-*.yml                                    │
│  • generated-macos-arm64-binary-*.yml                                       │
│  • generated-windows-binary-*.yml                                           │
│                                                                              │
│  UTILITIES:                                                                  │
│  • trymerge.yml / tryrebase.yml - Auto-merge/rebase PRs                    │
│  • nightly.yml - Nightly builds                                             │
│  • docker-*.yml - Docker image builds                                       │
│  • upload-test-stats*.yml - Test statistics                                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Key Test Categories

| Config Type | Description | Example Runner |
|-------------|-------------|----------------|
| `default` | Core PyTorch tests | linux.4xlarge.nvidia.gpu |
| `distributed` | Distributed training tests | linux.g4dn.12xlarge.nvidia.gpu |
| `jit_legacy` | Legacy JIT tests | linux.4xlarge.nvidia.gpu |
| `crossref` | Cross-reference tests | linux.2xlarge |
| `dynamo_wrapped` | TorchDynamo tests | linux.2xlarge |
| `nogpu_AVX512` | CPU AVX512 tests | linux.4xlarge |
| `nogpu_NO_AVX2` | CPU non-AVX2 tests | linux.4xlarge |
| `mps` | Metal Performance Shaders | macos-m1-* |
| `docs_test` | Documentation tests | linux.2xlarge |

## Workflow Generation

Binary workflows are **generated** from Jinja2 templates in `.github/templates/`:
- `linux_binary_build_workflow.yml.j2`
- `macos_binary_build_workflow.yml.j2`
- `windows_binary_build_workflow.yml.j2`

Run `.github/regenerate.sh` to regenerate workflows after template changes.

---

## User

I have seen at github, there are many jobs, such as linux-jammy-cpu-py3.10-gcc11-bazel-test, but you did not display, so please regenerate, and show more details 

---

## Assistant (Build · openrouter/pony-alpha · 30.0s)

_Thinking:_

The user wants me to show more details about the CI/CD architecture, including specific jobs that appear in GitHub Actions like "linux-jammy-cpu-py3.10-gcc11-bazel-test". I need to dig deeper into the workflow files to find all the job definitions and show a more comprehensive view.

Let me look at more workflow files to find all the job definitions.

**Tool: bash**

**Input:**
```json
{
  "command": "grep -h \"^\\s*linux-\\|^\\s*win-\\|^\\s*macos-\\|^\\s*libtorch-\" .github/workflows/pull.yml .github/workflows/trunk.yml .github/workflows/periodic.yml 2>/dev/null | sort | uniq | head -100",
  "description": "Extract all job names from main workflows",
  "workdir": "D:\\oss\\opensource\\pytorch-2.6.0"
}
```

**Output:**
```
  libtorch-linux-focal-cuda12_1-py3_7-gcc9-debug-build:
  libtorch-linux-focal-cuda12_4-py3_7-gcc9-debug-build:
  linux-docs:
  linux-focal-cpu-py3_10-gcc9-bazel-test:
  linux-focal-cuda11_8-py3_10-gcc9-build:
  linux-focal-cuda11_8-py3_10-gcc9-debug-build:
  linux-focal-cuda11_8-py3_10-gcc9-debug-test:
  linux-focal-cuda11_8-py3_10-gcc9-experimental-split-build-test:
  linux-focal-cuda11_8-py3_10-gcc9-experimental-split-build:
  linux-focal-cuda11_8-py3_10-gcc9-test:
  linux-focal-cuda11_8-py3_9-gcc9-build:
  linux-focal-cuda11_8-py3_9-gcc9-experimental-split-build-test:
  linux-focal-cuda11_8-py3_9-gcc9-experimental-split-build:
  linux-focal-cuda11_8-py3_9-gcc9-test:
  linux-focal-cuda12_1-py3-gcc9-slow-gradcheck-build:
  linux-focal-cuda12_1-py3-gcc9-slow-gradcheck-test:
  linux-focal-cuda12_1-py3_10-gcc9-build:
  linux-focal-cuda12_1-py3_10-gcc9-experimental-split-build-test:
  linux-focal-cuda12_1-py3_10-gcc9-experimental-split-build:
  linux-focal-cuda12_1-py3_10-gcc9-inductor-build:
  linux-focal-cuda12_1-py3_10-gcc9-no-ops-build:
  linux-focal-cuda12_1-py3_10-gcc9-test:
  linux-focal-cuda12_4-py3_10-gcc9-bazel-test:
  linux-focal-cuda12_4-py3_10-gcc9-build:
  linux-focal-cuda12_4-py3_10-gcc9-experimental-split-build-test:
  linux-focal-cuda12_4-py3_10-gcc9-experimental-split-build:
  linux-focal-cuda12_4-py3_10-gcc9-inductor-build:
  linux-focal-cuda12_4-py3_10-gcc9-inductor-test:
  linux-focal-cuda12_4-py3_10-gcc9-no-ops-build:
  linux-focal-cuda12_4-py3_10-gcc9-sm89-build:
  linux-focal-cuda12_4-py3_10-gcc9-sm89-test:
  linux-focal-cuda12_4-py3_10-gcc9-test:
  linux-focal-py3_11-clang10-build:
  linux-focal-py3_11-clang10-test:
  linux-focal-py3_12-clang10-build:
  linux-focal-py3_12-clang10-experimental-split-build-test:
  linux-focal-py3_12-clang10-experimental-split-build:
  linux-focal-py3_12-clang10-test:
  linux-focal-py3_13-clang10-build:
  linux-focal-py3_13-clang10-test:
  linux-focal-py3_9-clang10-build:
  linux-focal-py3_9-clang10-onnx-build:
  linux-focal-py3_9-clang10-onnx-test:
  linux-focal-py3_9-clang10-test:
  linux-focal-py3_9-clang9-xla-build:
  linux-focal-py3_9-clang9-xla-test:
  linux-focal-rocm6_2-py3_10-build:
  linux-focal-rocm6_2-py3_10-test:
  linux-jammy-cuda-11_8-cudnn9-py3_9-clang12-build:
  linux-jammy-py3-clang12-executorch-build:
  linux-jammy-py3-clang12-executorch-test:
  linux-jammy-py3-clang12-mobile-build:
  linux-jammy-py3_10-clang15-asan-build:
  linux-jammy-py3_10-clang15-asan-test:
  linux-jammy-py3_9-gcc11-build:
  linux-jammy-py3_9-gcc11-mobile-lightweight-dispatch-build:
  linux-jammy-py3_9-gcc11-no-ops:
  linux-jammy-py3_9-gcc11-pch:
  linux-jammy-py3_9-gcc11-test:
  macos-py3-arm64-build:
  macos-py3-arm64-mps-test:
  macos-py3-arm64-test:
  win-vs2019-cpu-py3-build:
  win-vs2019-cpu-py3-test:
  win-vs2019-cuda12_1-py3-build:

```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\pull.yml",
  "offset": 609
}
```

**Output:**
```
<file>


(End of file - total 609 lines)
</file>
```

---

## Assistant (Build · openrouter/pony-alpha · 74.3s)

_Thinking:_

Let me get more details about the inductor workflows and other specialized workflows to show a more comprehensive picture.

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\inductor.yml"
}
```

**Output:**
```
<file>
00001| # Workflow: Inductor
00002| # runs all inductor tests, including both benchmark tests and unit tests.
00003| # adding New Tests:
00004| #  1. inductor-unittest.yml:
00005| #      - Unit Tests
00006| #      - Mixed Tests
00007| #      - Flaky Benchmark tests
00008| #  2. inductor.yml(this workflow):
00009| #      - non-flaky benchmark tests
00010| name: inductor
00011| 
00012| on:
00013|   push:
00014|     branches:
00015|       - main
00016|       - release/*
00017|     tags:
00018|       - ciflow/inductor/*
00019|   workflow_dispatch:
00020| 
00021| concurrency:
00022|   group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref_name }}-${{ github.ref_type == 'branch' && github.sha }}-${{ github.event_name == 'workflow_dispatch' }}
00023|   cancel-in-progress: true
00024| 
00025| permissions: read-all
00026| 
00027| jobs:
00028|   unit-test:
00029|     if: github.repository_owner == 'pytorch'
00030|     name: unit-test
00031|     uses: ./.github/workflows/inductor-unittest.yml
00032|     secrets: inherit
00033| 
00034|   get-label-type:
00035|     name: get-label-type
00036|     uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
00037|     if: ${{ (github.event_name != 'schedule' || github.repository == 'pytorch/pytorch') && github.repository_owner == 'pytorch' }}
00038|     with:
00039|       triggering_actor: ${{ github.triggering_actor }}
00040|       issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
00041|       curr_branch: ${{ github.head_ref || github.ref_name }}
00042|       curr_ref_type: ${{ github.ref_type }}
00043| 
00044|   linux-focal-cuda12_4-py3_10-gcc9-inductor-build:
00045|     name: cuda12.4-py3.10-gcc9-sm86
00046|     uses: ./.github/workflows/_linux-build.yml
00047|     needs: get-label-type
00048|     with:
00049|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-sm86
00050|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9-inductor-benchmarks
00051|       cuda-arch-list: '8.6'
00052|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00053|       sync-tag: linux-focal-cuda12_4-py3_10-gcc9-inductor-build
00054|       test-matrix: |
00055|         { include: [
00056|           { config: "inductor_huggingface", shard: 1, num_shards: 1, runner: "linux.g5.4xlarge.nvidia.gpu" },
00057|           { config: "inductor_timm", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00058|           { config: "inductor_timm", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00059|           { config: "inductor_torchbench", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00060|           { config: "inductor_torchbench", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00061|         ]}
00062|     secrets: inherit
00063| 
00064|   linux-focal-cuda12_4-py3_10-gcc9-inductor-test:
00065|     name: cuda12.4-py3.10-gcc9-sm86
00066|     uses: ./.github/workflows/_linux-test.yml
00067|     needs: linux-focal-cuda12_4-py3_10-gcc9-inductor-build
00068|     with:
00069|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-sm86
00070|       docker-image: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-inductor-build.outputs.docker-image }}
00071|       test-matrix: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-inductor-build.outputs.test-matrix }}
00072|     secrets: inherit
00073| 
00074|   linux-jammy-cpu-py3_9-gcc11-inductor-build:
00075|     name: linux-jammy-cpu-py3.9-gcc11-inductor
00076|     uses: ./.github/workflows/_linux-build.yml
00077|     needs: get-label-type
00078|     with:
00079|       build-environment: linux-jammy-py3.9-gcc11-build
00080|       docker-image-name: pytorch-linux-jammy-py3.9-gcc11-inductor-benchmarks
00081|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00082|       sync-tag: linux-jammy-cpu-py3_9-gcc11-inductor-build
00083|       test-matrix: |
00084|         { include: [
00085|           { config: "cpu_inductor_torchbench", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00086|           { config: "cpu_inductor_torchbench", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00087|           { config: "dynamic_cpu_inductor_huggingface", shard: 1, num_shards: 1, runner: "linux.8xlarge.amx" },
00088|           { config: "dynamic_cpu_inductor_timm", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00089|           { config: "dynamic_cpu_inductor_timm", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00090|           { config: "dynamic_cpu_inductor_torchbench", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00091|           { config: "dynamic_cpu_inductor_torchbench", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00092|           { config: "inductor_torchbench_cpu_smoketest_perf", shard: 1, num_shards: 1, runner: "linux.24xl.spr-metal" },
00093|         ]}
00094|     secrets: inherit
00095| 
00096|   linux-jammy-cpu-py3_9-gcc11-inductor-test:
00097|     name: linux-jammy-cpu-py3.9-gcc11-inductor
00098|     uses: ./.github/workflows/_linux-test.yml
00099|     needs: linux-jammy-cpu-py3_9-gcc11-inductor-build
00100|     with:
00101|       build-environment: linux-jammy-py3.9-gcc11-build
00102|       docker-image: ${{ needs.linux-jammy-cpu-py3_9-gcc11-inductor-build.outputs.docker-image }}
00103|       test-matrix: ${{ needs.linux-jammy-cpu-py3_9-gcc11-inductor-build.outputs.test-matrix }}
00104|     secrets: inherit
00105| 

(End of file - total 105 lines)
</file>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\slow.yml"
}
```

**Output:**
```
<file>
00001| # This workflow is dedicated to host slow jobs that are run only periodically because
00002| # they are too slow to run in every commit.  The list of slow tests can be found in
00003| # https://github.com/pytorch/test-infra/blob/generated-stats/stats/slow-tests.json
00004| name: slow
00005| 
00006| on:
00007|   push:
00008|     branches:
00009|       - main
00010|       - release/*
00011|     tags:
00012|       - ciflow/slow/*
00013|   schedule:
00014|     - cron: 29 8 * * *  # about 1:29am PDT, for mem leak check and rerun disabled tests
00015|   workflow_dispatch:
00016| 
00017| concurrency:
00018|   group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref_name }}-${{ github.ref_type == 'branch' && github.sha }}-${{ github.event_name == 'workflow_dispatch' }}-${{ github.event_name == 'schedule' }}-${{ github.event.schedule }}
00019|   cancel-in-progress: true
00020| 
00021| permissions: read-all
00022| 
00023| jobs:
00024|   llm-td:
00025|     if: github.repository_owner == 'pytorch'
00026|     name: before-test
00027|     uses: ./.github/workflows/llm_td_retrieval.yml
00028|     permissions:
00029|       id-token: write
00030|       contents: read
00031| 
00032|   target-determination:
00033|     name: before-test
00034|     uses: ./.github/workflows/target_determination.yml
00035|     needs: llm-td
00036|     permissions:
00037|       id-token: write
00038|       contents: read
00039| 
00040|   get-label-type:
00041|     name: get-label-type
00042|     uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
00043|     if: ${{ (github.event_name != 'schedule' || github.repository == 'pytorch/pytorch') && github.repository_owner == 'pytorch' }}
00044|     with:
00045|       triggering_actor: ${{ github.triggering_actor }}
00046|       issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
00047|       curr_branch: ${{ github.head_ref || github.ref_name }}
00048|       curr_ref_type: ${{ github.ref_type }}
00049| 
00050|   linux-focal-cuda12_1-py3_10-gcc9-sm86-build:
00051|     name: linux-focal-cuda12.1-py3.10-gcc9-sm86
00052|     uses: ./.github/workflows/_linux-build.yml
00053|     needs: get-label-type
00054|     with:
00055|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00056|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-sm86
00057|       docker-image-name: pytorch-linux-focal-cuda12.1-cudnn9-py3-gcc9
00058|       cuda-arch-list: 8.6
00059|       test-matrix: |
00060|         { include: [
00061|           { config: "slow", shard: 1, num_shards: 3, runner: "linux.g5.4xlarge.nvidia.gpu" },
00062|           { config: "slow", shard: 2, num_shards: 3, runner: "linux.g5.4xlarge.nvidia.gpu" },
00063|           { config: "slow", shard: 3, num_shards: 3, runner: "linux.g5.4xlarge.nvidia.gpu" },
00064|         ]}
00065|     secrets: inherit
00066| 
00067|   linux-focal-cuda12_1-py3_10-gcc9-sm86-test:
00068|     name: linux-focal-cuda12.1-py3.10-gcc9-sm86
00069|     uses: ./.github/workflows/_linux-test.yml
00070|     needs:
00071|       - linux-focal-cuda12_1-py3_10-gcc9-sm86-build
00072|       - target-determination
00073|     with:
00074|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-sm86
00075|       docker-image: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-sm86-build.outputs.docker-image }}
00076|       test-matrix: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-sm86-build.outputs.test-matrix }}
00077|     secrets: inherit
00078| 
00079|   linux-focal-py3_9-clang10-build:
00080|     name: linux-focal-py3.9-clang10
00081|     uses: ./.github/workflows/_linux-build.yml
00082|     needs: get-label-type
00083|     with:
00084|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00085|       build-environment: linux-focal-py3.9-clang10
00086|       docker-image-name: pytorch-linux-focal-py3.9-clang10
00087|       test-matrix: |
00088|         { include: [
00089|           { config: "slow", shard: 1, num_shards: 2, runner: "linux.2xlarge" },
00090|           { config: "slow", shard: 2, num_shards: 2, runner: "linux.2xlarge" },
00091|         ]}
00092|     secrets: inherit
00093| 
00094|   linux-focal-py3_9-clang10-test:
00095|     name: linux-focal-py3.9-clang10
00096|     uses: ./.github/workflows/_linux-test.yml
00097|     needs:
00098|       - linux-focal-py3_9-clang10-build
00099|       - target-determination
00100|     with:
00101|       build-environment: linux-focal-py3.9-clang10
00102|       docker-image: ${{ needs.linux-focal-py3_9-clang10-build.outputs.docker-image }}
00103|       test-matrix: ${{ needs.linux-focal-py3_9-clang10-build.outputs.test-matrix }}
00104|     secrets: inherit
00105| 
00106|   linux-focal-rocm6_2-py3_10-build:
00107|     name: linux-focal-rocm6.2-py3.10
00108|     uses: ./.github/workflows/_linux-build.yml
00109|     needs: get-label-type
00110|     with:
00111|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00112|       build-environment: linux-focal-rocm6.2-py3.10
00113|       docker-image-name: pytorch-linux-focal-rocm-n-py3
00114|       test-matrix: |
00115|         { include: [
00116|           { config: "slow", shard: 1, num_shards: 2, runner: "linux.rocm.gpu", owners: ["module:rocm"] },
00117|           { config: "slow", shard: 2, num_shards: 2, runner: "linux.rocm.gpu", owners: ["module:rocm"] },
00118|         ]}
00119|     secrets: inherit
00120| 
00121|   linux-focal-rocm6_2-py3_10-test:
00122|     permissions:
00123|       id-token: write
00124|       contents: read
00125|     name: linux-focal-rocm6.2-py3.10
00126|     uses: ./.github/workflows/_rocm-test.yml
00127|     needs:
00128|       - linux-focal-rocm6_2-py3_10-build
00129|       - target-determination
00130|     with:
00131|       build-environment: linux-focal-rocm6.2-py3.10
00132|       docker-image: ${{ needs.linux-focal-rocm6_2-py3_10-build.outputs.docker-image }}
00133|       test-matrix: ${{ needs.linux-focal-rocm6_2-py3_10-build.outputs.test-matrix }}
00134|     secrets: inherit
00135| 
00136|   linux-jammy-py3_10-clang15-asan-build:
00137|     name: linux-jammy-py3.10-clang15-asan
00138|     uses: ./.github/workflows/_linux-build.yml
00139|     needs: get-label-type
00140|     with:
00141|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00142|       build-environment: linux-jammy-py3.10-clang15-asan
00143|       docker-image-name: pytorch-linux-jammy-py3-clang15-asan
00144|       test-matrix: |
00145|         { include: [
00146|           { config: "slow", shard: 1, num_shards: 3, runner: "linux.4xlarge" },
00147|           { config: "slow", shard: 2, num_shards: 3, runner: "linux.4xlarge" },
00148|           { config: "slow", shard: 3, num_shards: 3, runner: "linux.4xlarge" },
00149|         ]}
00150|       sync-tag: asan-build
00151|     secrets: inherit
00152| 
00153|   linux-jammy-py3_10-clang15-asan-test:
00154|     name: linux-jammy-py3.10-clang15-asan
00155|     uses: ./.github/workflows/_linux-test.yml
00156|     needs:
00157|       - linux-jammy-py3_10-clang15-asan-build
00158|       - target-determination
00159|     with:
00160|       build-environment: linux-jammy-py3.10-clang15-asan
00161|       docker-image: ${{ needs.linux-jammy-py3_10-clang15-asan-build.outputs.docker-image }}
00162|       test-matrix: ${{ needs.linux-jammy-py3_10-clang15-asan-build.outputs.test-matrix }}
00163|       sync-tag: asan-test
00164|     secrets: inherit
00165| 

(End of file - total 165 lines)
</file>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\inductor-unittest.yml"
}
```

**Output:**
```
<file>
00001| # Workflow: Inductor Unit Test
00002| # 1. runs unit tests for inductor.
00003| # 2. perfoms daily memory leak checks and reruns of disabled tests, scheduled at `29 8 * * *`.
00004| name: inductor-unittest
00005| 
00006| on:
00007|   workflow_call:
00008|   schedule:
00009|     - cron: 29 8 * * * # about 1:29am PDT, for mem leak check and rerun disabled tests.
00010| 
00011| concurrency:
00012|   group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref_name }}-${{ github.ref_type == 'branch' && github.sha }}-${{ github.event_name == 'workflow_dispatch' }}-unittest
00013|   cancel-in-progress: true
00014| 
00015| permissions: read-all
00016| 
00017| jobs:
00018|   get-label-type:
00019|     name: get-label-type
00020|     uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
00021|     if: ${{ (github.event_name != 'schedule' || github.repository == 'pytorch/pytorch') && github.repository_owner == 'pytorch' }}
00022|     with:
00023|       triggering_actor: ${{ github.triggering_actor }}
00024|       issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
00025|       curr_branch: ${{ github.head_ref || github.ref_name }}
00026|       curr_ref_type: ${{ github.ref_type }}
00027| 
00028|   linux-focal-cuda12_4-py3_10-gcc9-inductor-build:
00029|     name: cuda12.4-py3.10-gcc9-sm86
00030|     uses: ./.github/workflows/_linux-build.yml
00031|     needs: get-label-type
00032|     with:
00033|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-sm86
00034|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9-inductor-benchmarks
00035|       cuda-arch-list: '8.6'
00036|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00037|       test-matrix: |
00038|         { include: [
00039|           { config: "inductor", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00040|           { config: "inductor", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00041|           { config: "inductor_distributed", shard: 1, num_shards: 1, runner: "linux.g5.12xlarge.nvidia.gpu" },
00042|           { config: "inductor_cpp_wrapper", shard: 1, num_shards: 1, runner: "linux.g5.4xlarge.nvidia.gpu" },
00043|         ]}
00044|     secrets: inherit
00045| 
00046|   linux-focal-cuda12_4-py3_10-gcc9-inductor-test:
00047|     name: cuda12.4-py3.10-gcc9-sm86
00048|     uses: ./.github/workflows/_linux-test.yml
00049|     needs: linux-focal-cuda12_4-py3_10-gcc9-inductor-build
00050|     with:
00051|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-sm86
00052|       docker-image: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-inductor-build.outputs.docker-image }}
00053|       test-matrix: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-inductor-build.outputs.test-matrix }}
00054|     secrets: inherit
00055| 
00056|   linux-focal-cuda12_4-py3_12-gcc9-inductor-build:
00057|     name: cuda12.4-py3.12-gcc9-sm86
00058|     uses: ./.github/workflows/_linux-build.yml
00059|     needs: get-label-type
00060|     with:
00061|       build-environment: linux-focal-cuda12.4-py3.12-gcc9-sm86
00062|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3.12-gcc9-inductor-benchmarks
00063|       cuda-arch-list: '8.6'
00064|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00065|       test-matrix: |
00066|         { include: [
00067|           { config: "inductor", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00068|           { config: "inductor", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00069|         ]}
00070|     secrets: inherit
00071| 
00072|   linux-focal-cuda12_4-py3_12-gcc9-inductor-test:
00073|     name: cuda12.4-py3.12-gcc9-sm86
00074|     uses: ./.github/workflows/_linux-test.yml
00075|     needs: linux-focal-cuda12_4-py3_12-gcc9-inductor-build
00076|     with:
00077|       build-environment: linux-focal-cuda12.4-py3.12-gcc9-sm86
00078|       docker-image: ${{ needs.linux-focal-cuda12_4-py3_12-gcc9-inductor-build.outputs.docker-image }}
00079|       test-matrix: ${{ needs.linux-focal-cuda12_4-py3_12-gcc9-inductor-build.outputs.test-matrix }}
00080|     secrets: inherit
00081| 
00082|   linux-jammy-cpu-py3_12-inductor-halide-build:
00083|     name: linux-jammy-cpu-py3.12-gcc11-inductor-halide
00084|     uses: ./.github/workflows/_linux-build.yml
00085|     needs: get-label-type
00086|     with:
00087|       build-environment: linux-jammy-py3.12-gcc11
00088|       docker-image-name: pytorch-linux-jammy-py3.12-halide
00089|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00090|       test-matrix: |
00091|         { include: [
00092|           { config: "inductor-halide", shard: 1, num_shards: 1, runner: "linux.12xlarge" },
00093|         ]}
00094|     secrets: inherit
00095| 
00096|   linux-jammy-cpu-py3_12-inductor-halide-test:
00097|     name: linux-jammy-cpu-py3.12-gcc11-inductor-halide
00098|     uses: ./.github/workflows/_linux-test.yml
00099|     needs: linux-jammy-cpu-py3_12-inductor-halide-build
00100|     with:
00101|       build-environment: linux-jammy-py3.12-gcc11
00102|       docker-image: ${{ needs.linux-jammy-cpu-py3_12-inductor-halide-build.outputs.docker-image }}
00103|       test-matrix: ${{ needs.linux-jammy-cpu-py3_12-inductor-halide-build.outputs.test-matrix }}
00104|     secrets: inherit
00105| 
00106|   linux-jammy-cpu-py3_12-inductor-triton-cpu-build:
00107|     name: linux-jammy-cpu-py3.12-gcc11-inductor-triton-cpu
00108|     uses: ./.github/workflows/_linux-build.yml
00109|     needs: get-label-type
00110|     with:
00111|       build-environment: linux-jammy-py3.12-gcc11
00112|       docker-image-name: pytorch-linux-jammy-py3.12-triton-cpu
00113|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00114|       test-matrix: |
00115|         { include: [
00116|           { config: "inductor-triton-cpu", shard: 1, num_shards: 1, runner: "linux.12xlarge" },
00117|         ]}
00118|     secrets: inherit
00119| 
00120|   linux-jammy-cpu-py3_12-inductor-triton-cpu-test:
00121|     name: linux-jammy-cpu-py3.12-gcc11-inductor-triton-cpu
00122|     uses: ./.github/workflows/_linux-test.yml
00123|     needs: linux-jammy-cpu-py3_12-inductor-triton-cpu-build
00124|     with:
00125|       build-environment: linux-jammy-py3.12-gcc11
00126|       docker-image: ${{ needs.linux-jammy-cpu-py3_12-inductor-triton-cpu-build.outputs.docker-image }}
00127|       test-matrix: ${{ needs.linux-jammy-cpu-py3_12-inductor-triton-cpu-build.outputs.test-matrix }}
00128|     secrets: inherit
00129| 
00130|   linux-jammy-cpu-py3_9-gcc11-inductor-build:
00131|     name: linux-jammy-cpu-py3.9-gcc11-inductor
00132|     uses: ./.github/workflows/_linux-build.yml
00133|     needs: get-label-type
00134|     with:
00135|       build-environment: linux-jammy-py3.9-gcc11-build
00136|       docker-image-name: pytorch-linux-jammy-py3.9-gcc11-inductor-benchmarks
00137|       runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
00138|       test-matrix: |
00139|         { include: [
00140|           { config: "inductor_amx", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00141|           { config: "inductor_amx", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00142|           { config: "inductor_avx2", shard: 1, num_shards: 2, runner: "linux.10xlarge.avx2" },
00143|           { config: "inductor_avx2", shard: 2, num_shards: 2, runner: "linux.10xlarge.avx2" },
00144|         ]}
00145|     secrets: inherit
00146| 
00147|   linux-jammy-cpu-py3_9-gcc11-inductor-test:
00148|     name: linux-jammy-cpu-py3.9-gcc11-inductor
00149|     uses: ./.github/workflows/_linux-test.yml
00150|     needs: linux-jammy-cpu-py3_9-gcc11-inductor-build
00151|     with:
00152|       build-environment: linux-jammy-py3.9-gcc11-build
00153|       docker-image: ${{ needs.linux-jammy-cpu-py3_9-gcc11-inductor-build.outputs.docker-image }}
00154|       test-matrix: ${{ needs.linux-jammy-cpu-py3_9-gcc11-inductor-build.outputs.test-matrix }}
00155|     secrets: inherit
00156| 
00157|   linux-focal-cuda12_4-py3_13-gcc9-inductor-build:
00158|     name: cuda12.4-py3.13-gcc9-sm86
00159|     uses: ./.github/workflows/_linux-build.yml
00160|     needs: get-label-type
00161|     with:
00162|       build-environment: linux-focal-cuda12.4-py3.13-gcc9-sm86
00163|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3.13-gcc9-inductor-benchmarks
00164|       cuda-arch-list: '8.6'
00165|       test-matrix: |
00166|         { include: [
00167|           { config: "inductor", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00168|           { config: "inductor", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00169|         ]}
00170|     secrets: inherit
00171| 
00172|   linux-focal-cuda12_4-py3_13-gcc9-inductor-test:
00173|     name: cuda12.4-py3.13-gcc9-sm86
00174|     uses: ./.github/workflows/_linux-test.yml
00175|     needs: linux-focal-cuda12_4-py3_13-gcc9-inductor-build
00176|     with:
00177|       build-environment: linux-focal-cuda12.4-py3.13-gcc9-sm86
00178|       docker-image: ${{ needs.linux-focal-cuda12_4-py3_13-gcc9-inductor-build.outputs.docker-image }}
00179|       test-matrix: ${{ needs.linux-focal-cuda12_4-py3_13-gcc9-inductor-build.outputs.test-matrix }}
00180|     secrets: inherit
00181| 

(End of file - total 181 lines)
</file>
```

---

## Assistant (Build · openrouter/pony-alpha · 18.7s)

_Thinking:_

.
Let me also check the bazel workflow and some generated binary workflows to show the full picture.

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\_bazel-build-test.yml"
}
```

**Output:**
```
<file>
00001| name: bazel
00002| 
00003| on:
00004|   workflow_call:
00005|     inputs:
00006|       build-environment:
00007|         required: true
00008|         type: string
00009|         description: Top-level label for what's being built/tested.
00010|       docker-image-name:
00011|         required: true
00012|         type: string
00013|         description: Name of the base docker image to build with.
00014|       cuda-version:
00015|         required: true
00016|         type: string
00017|         description: What CUDA version to build with (i.e. "11.7"), "cpu" for none.
00018|       sync-tag:
00019|         required: false
00020|         type: string
00021|         default: ""
00022|         description: |
00023|           If this is set, our linter will use this to make sure that every other
00024|           job with the same `sync-tag` is identical.
00025|       test-matrix:
00026|         required: true
00027|         type: string
00028|         description: |
00029|           A JSON description of what configs to run later on.
00030|       runner:
00031|         required: false
00032|         type: string
00033|         default: "linux.large"
00034|         description: Runner type
00035| 
00036| env:
00037|   GIT_DEFAULT_BRANCH: ${{ github.event.repository.default_branch }}
00038| 
00039| jobs:
00040|   filter:
00041|     if: github.repository_owner == 'pytorch'
00042|     runs-on: ${{ inputs.runner }}
00043|     outputs:
00044|       test-matrix: ${{ steps.filter.outputs.test-matrix }}
00045|       is-test-matrix-empty: ${{ steps.filter.outputs.is-test-matrix-empty }}
00046|       keep-going: ${{ steps.filter.outputs.keep-going }}
00047|       reenabled-issues: ${{ steps.filter.outputs.reenabled-issues }}
00048|     steps:
00049|       - name: Checkout PyTorch
00050|         uses: pytorch/pytorch/.github/actions/checkout-pytorch@release/2.6
00051|         with:
00052|           fetch-depth: 1
00053|           submodules: false
00054| 
00055|       - name: Select all requested test configurations
00056|         id: filter
00057|         uses: ./.github/actions/filter-test-configs
00058|         with:
00059|           github-token: ${{ secrets.GITHUB_TOKEN }}
00060|           test-matrix: ${{ inputs.test-matrix }}
00061| 
00062|   build-and-test:
00063|     needs: filter
00064|     # Don't run on forked repos.
00065|     if: github.repository_owner == 'pytorch' && needs.filter.outputs.is-test-matrix-empty == 'False'
00066|     strategy:
00067|       matrix: ${{ fromJSON(needs.filter.outputs.test-matrix) }}
00068|       fail-fast: false
00069|     runs-on: ${{ matrix.runner }}
00070|     steps:
00071|       - name: Setup SSH (Click me for login details)
00072|         uses: pytorch/test-infra/.github/actions/setup-ssh@release/2.6
00073|         with:
00074|           github-secret: ${{ secrets.GITHUB_TOKEN }}
00075| 
00076|       # [see note: pytorch repo ref]
00077|       - name: Checkout PyTorch
00078|         uses: pytorch/pytorch/.github/actions/checkout-pytorch@release/2.6
00079| 
00080|       - name: Setup Linux
00081|         uses: ./.github/actions/setup-linux
00082| 
00083|       - name: Calculate docker image
00084|         id: calculate-docker-image
00085|         uses: pytorch/test-infra/.github/actions/calculate-docker-image@release/2.6
00086|         with:
00087|           docker-image-name: ${{ inputs.docker-image-name }}
00088| 
00089|       - name: Pull docker image
00090|         uses: pytorch/test-infra/.github/actions/pull-docker-image@release/2.6
00091|         with:
00092|           docker-image: ${{ steps.calculate-docker-image.outputs.docker-image }}
00093| 
00094|       - name: Check if in a container runner
00095|         shell: bash
00096|         id: check_container_runner
00097|         run: echo "IN_CONTAINER_RUNNER=$(if [ -f /.inarc ] || [ -f /.incontainer ]; then echo true ; else echo false; fi)" >> "$GITHUB_OUTPUT"
00098| 
00099|       - name: Install nvidia driver, nvidia-docker runtime, set GPU_FLAG
00100|         uses: pytorch/test-infra/.github/actions/setup-nvidia@release/2.6
00101|         if: ${{ inputs.cuda-version != 'cpu' && steps.check_container_runner.outputs.IN_CONTAINER_RUNNER == 'false' }}
00102| 
00103|       - name: Output disk space left
00104|         run: |
00105|           sudo df -H
00106| 
00107|       - name: Preserve github env variables for use in docker
00108|         run: |
00109|           env | grep '^GITHUB' >> "/tmp/github_env_${GITHUB_RUN_ID}"
00110|           env | grep '^CI' >> "/tmp/github_env_${GITHUB_RUN_ID}"
00111| 
00112|       - name: Parse ref
00113|         id: parse-ref
00114|         run: .github/scripts/parse_ref.py
00115| 
00116|       - name: Get workflow job id
00117|         id: get-job-id
00118|         uses: ./.github/actions/get-workflow-job-id
00119|         if: always()
00120|         with:
00121|           github-token: ${{ secrets.GITHUB_TOKEN }}
00122| 
00123|       - name: Build
00124|         env:
00125|           BUILD_ENVIRONMENT: ${{ inputs.build-environment }}
00126|           PR_NUMBER: ${{ github.event.pull_request.number }}
00127|           BRANCH: ${{ steps.parse-ref.outputs.branch }}
00128|           GITHUB_REPOSITORY: ${{ github.repository }}
00129|           GITHUB_WORKFLOW: ${{ github.workflow }}
00130|           GITHUB_JOB: ${{ github.job }}
00131|           GITHUB_RUN_ID: ${{ github.run_id }}
00132|           GITHUB_RUN_NUMBER: ${{ github.run_number }}
00133|           GITHUB_RUN_ATTEMPT: ${{ github.run_attempt }}
00134|           JOB_ID: ${{ steps.get-job-id.outputs.job-id }}
00135|           REENABLED_ISSUES: ${{ needs.filter.outputs.reenabled-issues }}
00136|           # TODO duplicated
00137|           AWS_DEFAULT_REGION: us-east-1
00138|           SHA1: ${{ github.event.pull_request.head.sha || github.sha }}
00139|           SCCACHE_BUCKET: ossci-compiler-cache-circleci-v2
00140|           SCCACHE_REGION: us-east-1
00141|           TORCH_CUDA_ARCH_LIST: 5.2
00142|           DOCKER_IMAGE: ${{ steps.calculate-docker-image.outputs.docker-image }}
00143|           OUR_GITHUB_JOB_ID: ${{ steps.get-job-id.outputs.job-id }}
00144|           CUDA_VERSION: ${{ inputs.cuda-version }}
00145|         run: |
00146|           export SHARD_NUMBER=0
00147|           # detached container should get cleaned up by teardown_ec2_linux
00148|           # TODO: Stop building test binaries as part of the build phase
00149|           # Make sure we copy test results from bazel-testlogs symlink to
00150|           # a regular directory ./test/test-reports
00151|           # shellcheck disable=SC2086
00152|           container_name=$(docker run \
00153|             ${GPU_FLAG:-} \
00154|             -e AWS_DEFAULT_REGION \
00155|             -e BUILD_ENVIRONMENT \
00156|             -e GITHUB_ACTIONS \
00157|             -e GITHUB_REPOSITORY \
00158|             -e GITHUB_WORKFLOW \
00159|             -e GITHUB_JOB \
00160|             -e GITHUB_RUN_NUMBER \
00161|             -e GITHUB_RUN_ATTEMPT \
00162|             -e JOB_ID \
00163|             -e GIT_DEFAULT_BRANCH="$GIT_DEFAULT_BRANCH" \
00164|             -e SHARD_NUMBER \
00165|             -e NUM_TEST_SHARDS \
00166|             -e MAX_JOBS="$(nproc --ignore=2)" \
00167|             -e SCCACHE_BUCKET \
00168|             -e SCCACHE_REGION \
00169|             -e SKIP_SCCACHE_INITIALIZATION=1 \
00170|             -e REENABLED_ISSUES \
00171|             -e TORCH_CUDA_ARCH_LIST \
00172|             -e OUR_GITHUB_JOB_ID \
00173|             -e CUDA_VERSION \
00174|             --env-file="/tmp/github_env_${GITHUB_RUN_ID}" \
00175|             --security-opt seccomp=unconfined \
00176|             --cap-add=SYS_PTRACE \
00177|             --shm-size="1g" \
00178|             --tty \
00179|             --detach \
00180|             --user jenkins \
00181|             -v "${GITHUB_WORKSPACE}:/var/lib/jenkins/workspace" \
00182|             -w /var/lib/jenkins/workspace \
00183|             "${DOCKER_IMAGE}"
00184|           )
00185|           docker exec -t "${container_name}" sh -c '.ci/pytorch/build.sh'
00186|           echo "container_id=${container_name}" >> "${GITHUB_ENV}"
00187| 
00188|       - name: Test
00189|         id: test
00190|         # Time out the test phase after 3.5 hours
00191|         timeout-minutes: 120
00192|         run: |
00193|           docker exec -t "${container_id}" sh -c '.ci/pytorch/test.sh && cp -Lr ./bazel-testlogs ./test/test-reports'
00194| 
00195|       - name: Print remaining test logs
00196|         shell: bash
00197|         if: always() && steps.test.conclusion
00198|         run: |
00199|           cat test/**/*_toprint.log || true
00200| 
00201|       - name: Chown workspace
00202|         uses: ./.github/actions/chown-workspace
00203|         if: always()
00204| 
00205|       - name: Upload test artifacts
00206|         uses: ./.github/actions/upload-test-artifacts
00207|         if: always() && steps.test.conclusion && steps.test.conclusion != 'skipped'
00208|         with:
00209|           file-suffix: bazel-${{ github.job }}_${{ steps.get-job-id.outputs.job-id }}
00210| 
00211|       - name: Teardown Linux
00212|         uses: pytorch/test-infra/.github/actions/teardown-linux@release/2.6
00213|         if: always()
00214| 

(End of file - total 214 lines)
</file>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\torchbench.yml"
}
```

**Output:**
```
<file>
00001| name: torchbench
00002| 
00003| on:
00004|   push:
00005|     tags:
00006|       - ciflow/torchbench/*
00007|   workflow_dispatch:
00008| 
00009| concurrency:
00010|   group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref_name }}-${{ github.ref_type == 'branch' && github.sha }}-${{ github.event_name == 'workflow_dispatch' }}-${{ github.event_name == 'schedule' }}
00011|   cancel-in-progress: true
00012| 
00013| jobs:
00014|   get-default-label-prefix:
00015|     if: github.repository_owner == 'pytorch'
00016|     name: get-default-label-prefix
00017|     uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
00018|     with:
00019|       triggering_actor: ${{ github.triggering_actor }}
00020|       issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
00021|       curr_branch: ${{ github.head_ref || github.ref_name }}
00022|       curr_ref_type: ${{ github.ref_type }}
00023| 
00024|   get-a100-test-label-type:
00025|     if: github.repository_owner == 'pytorch'
00026|     name: get-a100-test-label-type
00027|     uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
00028|     with:
00029|       triggering_actor: ${{ github.triggering_actor }}
00030|       issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
00031|       curr_branch: ${{ github.head_ref || github.ref_name }}
00032|       curr_ref_type: ${{ github.ref_type }}
00033|       check_experiments: "awsa100"
00034| 
00035|   linux-focal-cuda12_1-py3_10-gcc9-torchbench-build-gcp:
00036|     name: cuda12.1-py3.10-gcc9-sm80
00037|     uses: ./.github/workflows/_linux-build.yml
00038|     needs:
00039|       - get-default-label-prefix
00040|       - get-a100-test-label-type
00041|     with:
00042|       runner_prefix: "${{ needs.get-default-label-prefix.outputs.label-type }}"
00043|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-sm80
00044|       docker-image-name: pytorch-linux-focal-cuda12.1-cudnn9-py3-gcc9-inductor-benchmarks
00045|       cuda-arch-list: '8.0'
00046|       test-matrix: |
00047|         { include: [
00048|           { config: "torchbench_gcp_smoketest", shard: 1, num_shards: 1, runner: "${{ needs.get-a100-test-label-type.outputs.label-type }}linux.gcp.a100" },
00049|         ]}
00050|     secrets: inherit
00051| 
00052|   linux-focal-cuda12_1-py3_10-gcc9-torchbench-test-gcp:
00053|     name: cuda12.1-py3.10-gcc9-sm80
00054|     uses: ./.github/workflows/_linux-test.yml
00055|     needs: linux-focal-cuda12_1-py3_10-gcc9-torchbench-build-gcp
00056|     with:
00057|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-sm80
00058|       docker-image: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-torchbench-build-gcp.outputs.docker-image }}
00059|       test-matrix: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-torchbench-build-gcp.outputs.test-matrix }}
00060|       use-gha: anything-non-empty-to-use-gha
00061|     secrets: inherit
00062| 

(End of file - total 62 lines)
</file>
```

**Tool: bash**

**Input:**
```json
{
  "command": "head -100 .github/workflows/generated-linux-binary-manywheel-nightly.yml",
  "description": "View generated binary workflow header",
  "workdir": "D:\\oss\\opensource\\pytorch-2.6.0"
}
```

**Output:**
```
# @generated DO NOT EDIT MANUALLY

# Template is at:    .github/templates/linux_binary_build_workflow.yml.j2
# Generation script: .github/scripts/generate_ci_workflows.py
name: linux-binary-manywheel


on:
  push:
    # NOTE: Meta Employees can trigger new nightlies using: https://fburl.com/trigger_pytorch_nightly_build
    branches:
      - nightly
    tags:
      # NOTE: Binary build pipelines should only get triggered on release candidate builds
      # Release candidate tags look like: v1.11.0-rc1
      - v[0-9]+.[0-9]+.[0-9]+-rc[0-9]+
      - 'ciflow/binaries/*'
      - 'ciflow/binaries_wheel/*'
  workflow_dispatch:

env:
  # Needed for conda builds
  ALPINE_IMAGE: "308535385114.dkr.ecr.us-east-1.amazonaws.com/tool/alpine"
  ANACONDA_USER: pytorch
  AWS_DEFAULT_REGION: us-east-1
  BINARY_ENV_FILE: /tmp/env
  BUILD_ENVIRONMENT: linux-binary-manywheel
  BUILDER_ROOT: /builder
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  PR_NUMBER: ${{ github.event.pull_request.number }}
  PYTORCH_FINAL_PACKAGE_DIR: /artifacts
  PYTORCH_ROOT: /pytorch
  SHA1: ${{ github.event.pull_request.head.sha || github.sha }}
  SKIP_ALL_TESTS: 0
concurrency:
  group: linux-binary-manywheel-${{ github.event.pull_request.number || github.ref_name }}-${{ github.ref_type == 'branch' && github.sha }}-${{ github.event_name == 'workflow_dispatch' }}
  cancel-in-progress: true

jobs:
  get-label-type:
    if: github.repository_owner == 'pytorch'
    name: get-label-type
    uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
    with:
      triggering_actor: ${{ github.triggering_actor }}
      issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
      curr_branch: ${{ github.head_ref || github.ref_name }}
      curr_ref_type: ${{ github.ref_type }}
  manywheel-py3_9-cpu-build:
    if: ${{ github.repository_owner == 'pytorch' }}
    uses: ./.github/workflows/_binary-build-linux.yml
    needs: get-label-type
    with:
      PYTORCH_ROOT: /pytorch
      BUILDER_ROOT: /builder
      PACKAGE_TYPE: manywheel
      # TODO: This is a legacy variable that we eventually want to get rid of in
      #       favor of GPU_ARCH_VERSION
      DESIRED_CUDA: cpu
      GPU_ARCH_TYPE: cpu
      DOCKER_IMAGE: pytorch/manylinux-builder:cpu-2.6
      use_split_build: False
      DESIRED_PYTHON: "3.9"
      runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
      build_name: manywheel-py3_9-cpu
      build_environment: linux-binary-manywheel
    secrets:
      github-token: ${{ secrets.GITHUB_TOKEN }}
  manywheel-py3_9-cpu-test:  # Testing
    if: ${{ github.repository_owner == 'pytorch' }}
    needs:
      - manywheel-py3_9-cpu-build
      - get-label-type
    uses: ./.github/workflows/_binary-test-linux.yml
    with:
      PYTORCH_ROOT: /pytorch
      BUILDER_ROOT: /builder
      PACKAGE_TYPE: manywheel
      # TODO: This is a legacy variable that we eventually want to get rid of in
      #       favor of GPU_ARCH_VERSION
      DESIRED_CUDA: cpu
      GPU_ARCH_TYPE: cpu
      DOCKER_IMAGE: pytorch/manylinux-builder:cpu-2.6
      use_split_build: False
      DESIRED_PYTHON: "3.9"
      build_name: manywheel-py3_9-cpu
      build_environment: linux-binary-manywheel
      runner_prefix: "${{ needs.get-label-type.outputs.label-type }}"
      runs_on: linux.4xlarge
    secrets:
      github-token: ${{ secrets.GITHUB_TOKEN }}
  manywheel-py3_9-cpu-upload:  # Uploading
    if: ${{ github.repository_owner == 'pytorch' }}
    permissions:
      id-token: write
      contents: read
    needs: manywheel-py3_9-cpu-test
    with:
      PYTORCH_ROOT: /pytorch
      BUILDER_ROOT: /builder

```

---

## Assistant (Build · openrouter/pony-alpha · 22.4s)

_Thinking:_

Now let me also check the inductor-periodic workflow and any other important workflows to get a more complete picture. Let me also look at the binary workflows more closely.

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\inductor-periodic.yml"
}
```

**Output:**
```
<file>
00001| name: inductor-periodic
00002| 
00003| on:
00004|   push:
00005|     tags:
00006|       - ciflow/inductor-periodic/*
00007|   workflow_dispatch:
00008|   schedule:
00009|     # Run every 4 hours during the week and every 12 hours on the weekend
00010|     - cron: 45 0,4,8,12,16,20 * * 1-5
00011|     - cron: 45 4,12 * * 0,6
00012| 
00013| concurrency:
00014|   group: ${{ github.workflow }}-${{ github.event.pull_request.number || github.ref_name }}-${{ github.ref_type == 'branch' && github.sha }}-${{ github.event_name == 'workflow_dispatch' }}
00015|   cancel-in-progress: true
00016| 
00017| 
00018| permissions: read-all
00019| 
00020| jobs:
00021|   get-default-label-prefix:
00022|     name: get-default-label-prefix
00023|     uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
00024|     if: ${{ (github.event_name != 'schedule' || github.repository == 'pytorch/pytorch') && github.repository_owner == 'pytorch' }}
00025|     with:
00026|       triggering_actor: ${{ github.triggering_actor }}
00027|       issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
00028|       curr_branch: ${{ github.head_ref || github.ref_name }}
00029|       curr_ref_type: ${{ github.ref_type }}
00030| 
00031|   get-a100-test-label-type:
00032|     name: get-a100-test-label-type
00033|     uses: pytorch/pytorch/.github/workflows/_runner-determinator.yml@release/2.6
00034|     if: ${{ (github.event_name != 'schedule' || github.repository == 'pytorch/pytorch') && github.repository_owner == 'pytorch' }}
00035|     with:
00036|       triggering_actor: ${{ github.triggering_actor }}
00037|       issue_owner: ${{ github.event.pull_request.user.login || github.event.issue.user.login }}
00038|       curr_branch: ${{ github.head_ref || github.ref_name }}
00039|       curr_ref_type: ${{ github.ref_type }}
00040|       check_experiments: "awsa100"
00041| 
00042|   linux-focal-cuda12_1-py3_10-gcc9-periodic-dynamo-benchmarks-build:
00043|     name: cuda12.1-py3.10-gcc9-sm86-periodic-dynamo-benchmarks
00044|     uses: ./.github/workflows/_linux-build.yml
00045|     needs: get-default-label-prefix
00046|     with:
00047|       runner_prefix: "${{ needs.get-default-label-prefix.outputs.label-type }}"
00048|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-sm86
00049|       docker-image-name: pytorch-linux-focal-cuda12.1-cudnn9-py3-gcc9-inductor-benchmarks
00050|       cuda-arch-list: '8.6'
00051|       test-matrix: |
00052|         { include: [
00053|           { config: "dynamo_eager_torchbench", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00054|           { config: "dynamo_eager_torchbench", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00055|           { config: "dynamo_eager_huggingface", shard: 1, num_shards: 1, runner: "linux.g5.4xlarge.nvidia.gpu" },
00056|           { config: "dynamo_eager_timm", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00057|           { config: "dynamo_eager_timm", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00058|           { config: "aot_eager_torchbench", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00059|           { config: "aot_eager_torchbench", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00060|           { config: "aot_eager_huggingface", shard: 1, num_shards: 1, runner: "linux.g5.4xlarge.nvidia.gpu" },
00061|           { config: "aot_eager_timm", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00062|           { config: "aot_eager_timm", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00063|           { config: "dynamic_aot_eager_torchbench", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00064|           { config: "dynamic_aot_eager_torchbench", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00065|           { config: "dynamic_aot_eager_huggingface", shard: 1, num_shards: 1, runner: "linux.g5.4xlarge.nvidia.gpu" },
00066|           { config: "dynamic_aot_eager_timm", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00067|           { config: "dynamic_aot_eager_timm", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00068|         ]}
00069|     secrets: inherit
00070| 
00071|   linux-focal-cuda12_1-py3_10-gcc9-periodic-dynamo-benchmarks-test:
00072|     name: cuda12.1-py3.10-gcc9-sm86-periodic-dynamo-benchmarks
00073|     uses: ./.github/workflows/_linux-test.yml
00074|     needs: linux-focal-cuda12_1-py3_10-gcc9-periodic-dynamo-benchmarks-build
00075|     with:
00076|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-sm86
00077|       docker-image: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-periodic-dynamo-benchmarks-build.outputs.docker-image }}
00078|       test-matrix: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-periodic-dynamo-benchmarks-build.outputs.test-matrix }}
00079|     secrets: inherit
00080| 
00081|   linux-focal-cuda12_1-py3_10-gcc9-inductor-build-gcp:
00082|     name: cuda12.1-py3.10-gcc9-sm80
00083|     uses: ./.github/workflows/_linux-build.yml
00084|     needs:
00085|       - get-default-label-prefix
00086|       - get-a100-test-label-type
00087|     with:
00088|       runner_prefix: "${{ needs.get-default-label-prefix.outputs.label-type }}"
00089|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-sm80
00090|       docker-image-name: pytorch-linux-focal-cuda12.1-cudnn9-py3-gcc9-inductor-benchmarks
00091|       cuda-arch-list: '8.0'
00092|       test-matrix: |
00093|         { include: [
00094|           { config: "inductor_torchbench_smoketest_perf", shard: 1, num_shards: 1, runner: "${{ needs.get-a100-test-label-type.outputs.label-type }}linux.gcp.a100" },
00095|         ]}
00096|     secrets: inherit
00097| 
00098|   linux-focal-cuda12_1-py3_10-gcc9-inductor-test-gcp:
00099|     name: cuda12.1-py3.10-gcc9-sm80
00100|     uses: ./.github/workflows/_linux-test.yml
00101|     needs: linux-focal-cuda12_1-py3_10-gcc9-inductor-build-gcp
00102|     with:
00103|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-sm80
00104|       docker-image: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-inductor-build-gcp.outputs.docker-image }}
00105|       test-matrix: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-inductor-build-gcp.outputs.test-matrix }}
00106|       use-gha: anything-non-empty-to-use-gha
00107|       # disable monitor in smoke perf tests for more investigation
00108|       disable-monitor: true
00109|     secrets: inherit
00110| 
00111|   linux-jammy-cpu-py3_9-gcc11-periodic-dynamo-benchmarks-build:
00112|     name: linux-jammy-cpu-py3.9-gcc11-periodic-dynamo-benchmarks
00113|     uses: ./.github/workflows/_linux-build.yml
00114|     needs: get-default-label-prefix
00115|     with:
00116|       build-environment: linux-jammy-py3.9-gcc11-build
00117|       docker-image-name: pytorch-linux-jammy-py3.9-gcc11-inductor-benchmarks
00118|       runner_prefix: "${{ needs.get-default-label-prefix.outputs.label-type }}"
00119|       test-matrix: |
00120|         { include: [
00121|           { config: "cpu_inductor_huggingface", shard: 1, num_shards: 1, runner: "linux.8xlarge.amx" },
00122|           { config: "cpu_inductor_timm", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00123|           { config: "cpu_inductor_timm", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00124|           { config: "dynamic_cpu_inductor_huggingface", shard: 1, num_shards: 1, runner: "linux.8xlarge.amx" },
00125|           { config: "dynamic_cpu_inductor_timm", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00126|           { config: "dynamic_cpu_inductor_timm", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00127|           { config: "cpu_inductor_freezing_avx2_huggingface", shard: 1, num_shards: 1, runner: "linux.10xlarge.avx2" },
00128|           { config: "cpu_inductor_freezing_avx2_torchbench", shard: 1, num_shards: 2, runner: "linux.10xlarge.avx2" },
00129|           { config: "cpu_inductor_freezing_avx2_torchbench", shard: 2, num_shards: 2, runner: "linux.10xlarge.avx2" },
00130|           { config: "cpu_inductor_freezing_avx2_timm", shard: 1, num_shards: 2, runner: "linux.10xlarge.avx2" },
00131|           { config: "cpu_inductor_freezing_avx2_timm", shard: 2, num_shards: 2, runner: "linux.10xlarge.avx2" },
00132|         ]}
00133|     secrets: inherit
00134| 
00135|   linux-jammy-cpu-py3_9-gcc11-periodic-dynamo-benchmarks-test:
00136|     name: linux-jammy-cpu-py3.9-gcc11-periodic-dynamo-benchmarks
00137|     uses: ./.github/workflows/_linux-test.yml
00138|     needs: linux-jammy-cpu-py3_9-gcc11-periodic-dynamo-benchmarks-build
00139|     with:
00140|       build-environment: linux-jammy-py3.9-gcc11-build
00141|       docker-image: ${{ needs.linux-jammy-cpu-py3_9-gcc11-periodic-dynamo-benchmarks-build.outputs.docker-image }}
00142|       test-matrix: ${{ needs.linux-jammy-cpu-py3_9-gcc11-periodic-dynamo-benchmarks-build.outputs.test-matrix }}
00143|     secrets: inherit
00144| 
00145| 
00146|   linux-focal-cuda12_1-py3_10-gcc9-inductor-build:
00147|     name: cuda12.1-py3.10-gcc9-sm86
00148|     uses: ./.github/workflows/_linux-build.yml
00149|     needs: get-default-label-prefix
00150|     with:
00151|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-sm86
00152|       docker-image-name: pytorch-linux-focal-cuda12.1-cudnn9-py3-gcc9-inductor-benchmarks
00153|       cuda-arch-list: '8.6'
00154|       runner_prefix: "${{ needs.get-default-label-prefix.outputs.label-type }}"
00155|       sync-tag: linux-focal-cuda12_1-py3_10-gcc9-inductor-build
00156|       test-matrix: |
00157|         { include: [
00158|           { config: "dynamic_inductor_huggingface", shard: 1, num_shards: 1, runner: "linux.g5.4xlarge.nvidia.gpu" },
00159|           { config: "dynamic_inductor_timm", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00160|           { config: "dynamic_inductor_timm", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00161|           { config: "dynamic_inductor_torchbench", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00162|           { config: "dynamic_inductor_torchbench", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00163|           { config: "aot_inductor_huggingface", shard: 1, num_shards: 1, runner: "linux.g5.4xlarge.nvidia.gpu" },
00164|           { config: "aot_inductor_timm", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00165|           { config: "aot_inductor_timm", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00166|           { config: "aot_inductor_torchbench", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00167|           { config: "aot_inductor_torchbench", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00168|         ]}
00169|     secrets: inherit
00170| 
00171|   linux-focal-cuda12_1-py3_10-gcc9-inductor-test:
00172|     name: cuda12.1-py3.10-gcc9-sm86
00173|     uses: ./.github/workflows/_linux-test.yml
00174|     needs: linux-focal-cuda12_1-py3_10-gcc9-inductor-build
00175|     with:
00176|       build-environment: linux-focal-cuda12.1-py3.10-gcc9-sm86
00177|       docker-image: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-inductor-build.outputs.docker-image }}
00178|       test-matrix: ${{ needs.linux-focal-cuda12_1-py3_10-gcc9-inductor-build.outputs.test-matrix }}
00179|     secrets: inherit
00180| 
00181|   linux-focal-cuda12_4-py3_10-gcc9-inductor-build:
00182|     # Should be synced with the benchmark tests in inductor.yml, but this doesn't run inductor_timm
00183|     name: cuda12.4-py3.10-gcc9-sm86
00184|     uses: ./.github/workflows/_linux-build.yml
00185|     needs: get-default-label-prefix
00186|     with:
00187|       runner_prefix: "${{ needs.get-default-label-prefix.outputs.label-type }}"
00188|       sync-tag: linux-focal-cuda12_4-py3_10-gcc9-inductor-build
00189|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-sm86
00190|       docker-image-name: pytorch-linux-focal-cuda12.4-cudnn9-py3-gcc9-inductor-benchmarks
00191|       cuda-arch-list: '8.6'
00192|       test-matrix: |
00193|         { include: [
00194|           { config: "dynamic_inductor_huggingface", shard: 1, num_shards: 1, runner: "linux.g5.4xlarge.nvidia.gpu" },
00195|           { config: "dynamic_inductor_timm", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00196|           { config: "dynamic_inductor_timm", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00197|           { config: "dynamic_inductor_torchbench", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00198|           { config: "dynamic_inductor_torchbench", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00199|           { config: "aot_inductor_huggingface", shard: 1, num_shards: 1, runner: "linux.g5.4xlarge.nvidia.gpu" },
00200|           { config: "aot_inductor_timm", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00201|           { config: "aot_inductor_timm", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00202|           { config: "aot_inductor_torchbench", shard: 1, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00203|           { config: "aot_inductor_torchbench", shard: 2, num_shards: 2, runner: "linux.g5.4xlarge.nvidia.gpu" },
00204|         ]}
00205|     secrets: inherit
00206| 
00207|   linux-focal-cuda12_4-py3_10-gcc9-inductor-test:
00208|     name: cuda12.4-py3.10-gcc9-sm86
00209|     uses: ./.github/workflows/_linux-test.yml
00210|     needs: linux-focal-cuda12_4-py3_10-gcc9-inductor-build
00211|     with:
00212|       sync-tag: linux-focal-cuda12_4-py3_10-gcc9-inductor-test
00213|       build-environment: linux-focal-cuda12.4-py3.10-gcc9-sm86
00214|       docker-image: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-inductor-build.outputs.docker-image }}
00215|       test-matrix: ${{ needs.linux-focal-cuda12_4-py3_10-gcc9-inductor-build.outputs.test-matrix }}
00216|     secrets: inherit
00217| 
00218| 
00219|   linux-jammy-cpu-py3_9-gcc11-inductor-build:
00220|     name: linux-jammy-cpu-py3.9-gcc11-inductor
00221|     uses: ./.github/workflows/_linux-build.yml
00222|     needs: get-default-label-prefix
00223|     with:
00224|       build-environment: linux-jammy-py3.9-gcc11-build
00225|       docker-image-name: pytorch-linux-jammy-py3.9-gcc11-inductor-benchmarks
00226|       runner_prefix: "${{ needs.get-default-label-prefix.outputs.label-type }}"
00227|       sync-tag: linux-jammy-cpu-py3_9-gcc11-inductor-build
00228|       test-matrix: |
00229|         { include: [
00230|           { config: "cpu_inductor_freezing_huggingface", shard: 1, num_shards: 1, runner: "linux.8xlarge.amx" },
00231|           { config: "cpu_inductor_freezing_timm", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00232|           { config: "cpu_inductor_freezing_timm", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00233|           { config: "cpu_inductor_freezing_torchbench", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00234|           { config: "cpu_inductor_freezing_torchbench", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00235|           { config: "cpu_inductor_amp_freezing_huggingface", shard: 1, num_shards: 1, runner: "linux.8xlarge.amx" },
00236|           { config: "cpu_inductor_amp_freezing_timm", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00237|           { config: "cpu_inductor_amp_freezing_timm", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00238|           { config: "cpu_inductor_amp_freezing_torchbench", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00239|           { config: "cpu_inductor_amp_freezing_torchbench", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00240|           { config: "cpu_aot_inductor_freezing_huggingface", shard: 1, num_shards: 1, runner: "linux.8xlarge.amx" },
00241|           { config: "cpu_aot_inductor_freezing_timm", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00242|           { config: "cpu_aot_inductor_freezing_timm", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00243|           { config: "cpu_aot_inductor_freezing_torchbench", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00244|           { config: "cpu_aot_inductor_freezing_torchbench", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00245|           { config: "cpu_aot_inductor_amp_freezing_torchbench", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00246|           { config: "cpu_aot_inductor_amp_freezing_torchbench", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00247|           { config: "dynamic_cpu_aot_inductor_freezing_torchbench", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00248|           { config: "dynamic_cpu_aot_inductor_freezing_torchbench", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00249|           { config: "dynamic_cpu_aot_inductor_amp_freezing_torchbench", shard: 1, num_shards: 2, runner: "linux.8xlarge.amx" },
00250|           { config: "dynamic_cpu_aot_inductor_amp_freezing_torchbench", shard: 2, num_shards: 2, runner: "linux.8xlarge.amx" },
00251|         ]}
00252|     secrets: inherit
00253| 
00254|   linux-jammy-cpu-py3_9-gcc11-inductor-test:
00255|     name: linux-jammy-cpu-py3.9-gcc11-inductor
00256|     uses: ./.github/workflows/_linux-test.yml
00257|     needs: linux-jammy-cpu-py3_9-gcc11-inductor-build
00258|     with:
00259|       build-environment: linux-jammy-py3.9-gcc11-build
00260|       docker-image: ${{ needs.linux-jammy-cpu-py3_9-gcc11-inductor-build.outputs.docker-image }}
00261|       test-matrix: ${{ needs.linux-jammy-cpu-py3_9-gcc11-inductor-build.outputs.test-matrix }}
00262|     secrets: inherit
00263| 

(End of file - total 263 lines)
</file>
```

**Tool: read**

**Input:**
```json
{
  "filePath": "D:\\oss\\opensource\\pytorch-2.6.0\\.github\\workflows\\_runner-determinator.yml"
}
```

**Output:**
```
<file>
00001| name: Check whether the workflow owner can use ARC runners
00002| 
00003| on:
00004|   workflow_call:
00005|     inputs:
00006|       check_experiments:
00007|         required: false
00008|         type: string
00009|         description: |
00010|           List of experiments for this workfow. If not defined, all default experiments are included.
00011|       triggering_actor:
00012|         required: true
00013|         type: string
00014|         description: The triggering_actor for the workflow. Use github.triggering_actor
00015|       issue_owner:
00016|         required: true
00017|         type: string
00018|         description: The owner of the issue. Use github.event.pull_request.user.login || github.event.issue.user.login
00019|       curr_branch:
00020|         required: true
00021|         type: string
00022|         description: Current branch or tag.
00023|       curr_ref_type:
00024|         required: false
00025|         type: string
00026|         default: branch
00027|         description: The value of "github.ref_type", "branch" or "tag"
00028|       issue_number:
00029|         required: false
00030|         type: string
00031|         default: "5132"
00032|         description: |
00033|           Fetch's GitHub Issue from pytorch/test-infra
00034|           Example: https://github.com/pytorch/test-infra/issues/5132
00035| 
00036|     outputs:
00037|       label-type:
00038|         description: Type of runners to use
00039|         value: ${{ jobs.runner-determinator.outputs.label-type }}
00040| 
00041| jobs:
00042|   runner-determinator:
00043|     # Don't run on forked repos
00044|     if: github.repository_owner == 'pytorch'
00045|     runs-on: ubuntu-latest
00046|     outputs:
00047|       label-type: ${{ steps.set-condition.outputs.label-type }}
00048|     env:
00049|       GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
00050|       ISSUE_NUMBER: ${{ inputs.issue_number }}
00051|       TRIGGERING_ACTOR: ${{ inputs.triggering_actor }}
00052|       ISSUE_OWNER: ${{ inputs.issue_owner }}
00053|       CHECK_EXPERIMENTS: ${{ inputs.check_experiments }}
00054|       PR_NUMBER: ${{ github.event.pull_request.number }}
00055|     steps:
00056|       # - name: Checkout PyTorch
00057|       #   uses: pytorch/pytorch/.github/actions/checkout-pytorch@release/2.6
00058|       #   with:
00059|       #     fetch-depth: 1
00060|       #     submodules: true
00061| 
00062|       # TODO: Remove the hardcoded step below
00063|       # Hardcoding below is temporary for testing ALI runners
00064|       # This file below should match the script found in .github/scripts/runner_determinator.py
00065|       - name: Hardcode runner-determinator script
00066|         id: hardcode-script
00067|         run: |
00068|           cat <<EOF > runner_determinator.py
00069|           # flake8: noqa: G004
00070| 
00071|           # Note: Copies of this script in runner_determinator.py and _runner-determinator.yml
00072|           #       must be kept in sync. You can do it easily by running the following command:
00073|           #           python .github/scripts/update_runner_determinator.py
00074| 
00075|           """
00076|           This runner determinator is used to determine which set of runners to run a
00077|           GitHub job on. It uses the first comment of a GitHub issue (by default
00078|           https://github.com/pytorch/test-infra/issues/5132) to define the configuration
00079|           of which runners should be used to run which job.
00080| 
00081|           The configuration has two parts, the settings and a list of opted-in users,
00082|           separated by a line containing "---".  If the line is not present, the
00083|           settings are considered to be empty with only the second part, the user
00084|           list, defined.
00085| 
00086|           The first part is a YAML block that defines the rollout settings. This can be
00087|           used to define any settings that are needed to determine which runners to use.
00088|           It's fields are defined by the RolloutSettings class below.
00089| 
00090|           The second part is a list of users who are explicitly opted in to the LF fleet.
00091|           The user list is also a comma separated list of additional features or
00092|           experiments which the user could be opted in to.
00093| 
00094|           The user list has the following rules:
00095| 
00096|           - Users are GitHub usernames, which must start with the @ prefix
00097|           - Each user is also a comma-separated list of features/experiments to enable
00098|           - A "#" prefix opts the user out of all experiments
00099| 
00100|           Example config:
00101|               # A list of experiments that can be opted into.
00102|               # This defines the behavior they'll induce when opted into.
00103|               # Expected syntax is:
00104|               #   [experiment_name]: # Name of the experiment. Also used for the label prefix.
00105|               #      rollout_perc: [int] # % of workflows to run with this experiment when users are not opted in.
00106| 
00107|               experiments:
00108|                 lf:
00109|                   rollout_percent: 25
00110|                   all_branches: false
00111|                   default: true
00112|               ---
00113| 
00114|               # Opt-ins:
00115|               # Users can opt into the LF fleet by adding their GitHub username to this list
00116|               # and specifying experiments to enable in a comma-separated list.
00117|               # To always opt out of an experiment, prefix it with a "-".
00118|               # Experiments should be from the above list.
00119| 
00120|               @User1,-lf,split_build
00121|               @User2,lf
00122|               @User3,split_build
00123|           """
00124| 
00125|           import json
00126|           import logging
00127|           import os
00128|           import random
00129|           import re
00130|           import sys
00131|           from argparse import ArgumentParser
00132|           from functools import lru_cache
00133|           from logging import LogRecord
00134|           from typing import Any, Dict, FrozenSet, Iterable, List, NamedTuple, Set, Tuple
00135|           from urllib.request import Request, urlopen
00136| 
00137|           import yaml
00138|           from github import Auth, Github
00139|           from github.Issue import Issue
00140| 
00141| 
00142|           DEFAULT_LABEL_PREFIX = ""  # use meta runners
00143|           WORKFLOW_LABEL_LF = "lf."  # use runners from the linux foundation
00144|           WORKFLOW_LABEL_LF_CANARY = "lf.c."  # use canary runners from the linux foundation
00145| 
00146|           GITHUB_OUTPUT = os.getenv("GITHUB_OUTPUT", "")
00147|           GH_OUTPUT_KEY_AMI = "runner-ami"
00148|           GH_OUTPUT_KEY_LABEL_TYPE = "label-type"
00149|           OPT_OUT_LABEL = "no-runner-experiments"
00150| 
00151|           SETTING_EXPERIMENTS = "experiments"
00152| 
00153|           LF_FLEET_EXPERIMENT = "lf"
00154|           CANARY_FLEET_SUFFIX = ".c"
00155| 
00156| 
00157|           class Experiment(NamedTuple):
00158|               rollout_perc: float = (
00159|                   0  # Percentage of workflows to experiment on when user is not opted-in.
00160|               )
00161|               all_branches: bool = (
00162|                   False  # If True, the experiment is also enabled on the exception branches
00163|               )
00164|               default: bool = (
00165|                   True  # If True, the experiment is enabled by default for all queries
00166|               )
00167| 
00168|               # Add more fields as needed
00169| 
00170| 
00171|           class Settings(NamedTuple):
00172|               """
00173|               Settings for the experiments that can be opted into.
00174|               """
00175| 
00176|               experiments: Dict[str, Experiment] = {}
00177| 
00178| 
00179|           class ColorFormatter(logging.Formatter):
00180|               """Color codes the log messages based on the log level"""
00181| 
00182|               COLORS = {
00183|                   "WARNING": "\033[33m",  # Yellow
00184|                   "ERROR": "\033[31m",  # Red
00185|                   "CRITICAL": "\033[31m",  # Red
00186|                   "INFO": "\033[0m",  # Reset
00187|                   "DEBUG": "\033[0m",  # Reset
00188|               }
00189| 
00190|               def format(self, record: LogRecord) -> str:
00191|                   log_color = self.COLORS.get(record.levelname, "\033[0m")  # Default to reset
00192|                   record.msg = f"{log_color}{record.msg}\033[0m"
00193|                   return super().format(record)
00194| 
00195| 
00196|           handler = logging.StreamHandler()
00197|           handler.setFormatter(ColorFormatter(fmt="%(levelname)-8s: %(message)s"))
00198| 
00199|           log = logging.getLogger(os.path.basename(__file__))
00200|           log.addHandler(handler)
00201|           log.setLevel(logging.INFO)
00202| 
00203| 
00204|           def set_github_output(key: str, value: str) -> None:
00205|               """
00206|               Defines outputs of the github action that invokes this script
00207|               """
00208|               if not GITHUB_OUTPUT:
00209|                   # See https://github.blog/changelog/2022-10-11-github-actions-deprecating-save-state-and-set-output-commands/ for deprecation notice
00210|                   log.warning(
00211|                       "No env var found for GITHUB_OUTPUT, you must be running this code locally. Falling back to the deprecated print method."
00212|                   )
00213|                   print(f"::set-output name={key}::{value}")
00214|                   return
00215| 
00216|               with open(GITHUB_OUTPUT, "a") as f:
00217|                   log.info(f"Setting output: {key}='{value}'")
00218|                   f.write(f"{key}={value}\n")
00219| 
00220| 
00221|           def _str_comma_separated_to_set(value: str) -> FrozenSet[str]:
00222|               return frozenset(
00223|                   filter(lambda itm: itm != "", map(str.strip, value.strip(" \n\t").split(",")))
00224|               )
00225| 
00226| 
00227|           def parse_args() -> Any:
00228|               parser = ArgumentParser("Get dynamic rollout settings")
00229|               parser.add_argument("--github-token", type=str, required=True, help="GitHub token")
00230|               parser.add_argument(
00231|                   "--github-issue-repo",
00232|                   type=str,
00233|                   required=False,
00234|                   default="pytorch/test-infra",
00235|                   help="GitHub repo to get the issue",
00236|               )
00237|               parser.add_argument(
00238|                   "--github-repo",
00239|                   type=str,
00240|                   required=True,
00241|                   help="GitHub repo where CI is running",
00242|               )
00243|               parser.add_argument(
00244|                   "--github-issue", type=int, required=True, help="GitHub issue number"
00245|               )
00246|               parser.add_argument(
00247|                   "--github-actor", type=str, required=True, help="GitHub triggering_actor"
00248|               )
00249|               parser.add_argument(
00250|                   "--github-issue-owner", type=str, required=True, help="GitHub issue owner"
00251|               )
00252|               parser.add_argument(
00253|                   "--github-branch", type=str, required=True, help="Current GitHub branch or tag"
00254|               )
00255|               parser.add_argument(
00256|                   "--github-ref-type",
00257|                   type=str,
00258|                   required=True,
00259|                   help="Current GitHub ref type, branch or tag",
00260|               )
00261|               parser.add_argument(
00262|                   "--eligible-experiments",
00263|                   type=_str_comma_separated_to_set,
00264|                   required=False,
00265|                   default="",
00266|                   help="comma separated list of experiments to check, if omitted all experiments marked with default=True are checked",
00267|               )
00268|               parser.add_argument(
00269|                   "--pr-number",
00270|                   type=str,
00271|                   required=False,
00272|                   default="",
00273|                   help="the optional PR number where this is run",
00274|               )
00275| 
00276|               return parser.parse_args()
00277| 
00278| 
00279|           def get_gh_client(github_token: str) -> Github:
00280|               auth = Auth.Token(github_token)
00281|               return Github(auth=auth)
00282| 
00283| 
00284|           def get_issue(gh: Github, repo: str, issue_num: int) -> Issue:
00285|               repo = gh.get_repo(repo)
00286|               return repo.get_issue(number=issue_num)
00287| 
00288| 
00289|           def get_potential_pr_author(
00290|               github_token: str, repo: str, username: str, ref_type: str, ref_name: str
00291|           ) -> str:
00292|               # If the trigger was a new tag added by a bot, this is a ciflow case
00293|               # Fetch the actual username from the original PR. The PR number is
00294|               # embedded in the tag name: ciflow/<name>/<pr-number>
00295| 
00296|               gh = get_gh_client(github_token)
00297| 
00298|               if username == "pytorch-bot[bot]" and ref_type == "tag":
00299|                   split_tag = ref_name.split("/")
00300|                   if (
00301|                       len(split_tag) == 3
00302|                       and split_tag[0] == "ciflow"
00303|                       and split_tag[2].isnumeric()
00304|                   ):
00305|                       pr_number = split_tag[2]
00306|                       try:
00307|                           repository = gh.get_repo(repo)
00308|                           pull = repository.get_pull(number=int(pr_number))
00309|                       except Exception as e:
00310|                           raise Exception(  # noqa: TRY002
00311|                               f"issue with pull request {pr_number} from repo {repository}"
00312|                           ) from e
00313|                       return pull.user.login
00314|               # In all other cases, return the original input username
00315|               return username
00316| 
00317| 
00318|           def is_exception_branch(branch: str) -> bool:
00319|               """
00320|               Branches that get opted out of experiments by default, until they're explicitly enabled.
00321|               """
00322|               return branch.split("/")[0] in {"main", "nightly", "release", "landchecks"}
00323| 
00324| 
00325|           def load_yaml(yaml_text: str) -> Any:
00326|               try:
00327|                   data = yaml.safe_load(yaml_text)
00328|                   return data
00329|               except yaml.YAMLError:
00330|                   log.exception("Error loading YAML")
00331|                   raise
00332| 
00333| 
00334|           def extract_settings_user_opt_in_from_text(rollout_state: str) -> Tuple[str, str]:
00335|               """
00336|               Extracts the text with settings, if any, and the opted in users from the rollout state.
00337| 
00338|               If the issue body contains "---" then the text above that is the settings
00339|               and the text below is the list of opted in users.
00340| 
00341|               If it doesn't contain "---" then the settings are empty and the rest is the users.
00342|               """
00343|               rollout_state_parts = rollout_state.split("---")
00344|               if len(rollout_state_parts) >= 2:
00345|                   return rollout_state_parts[0], rollout_state_parts[1]
00346|               else:
00347|                   return "", rollout_state
00348| 
00349| 
00350|           class UserOptins(Dict[str, List[str]]):
00351|               """
00352|               Dictionary of users with a list of features they have opted into
00353|               """
00354| 
00355| 
00356|           def parse_user_opt_in_from_text(user_optin_text: str) -> UserOptins:
00357|               """
00358|               Parse the user opt-in text into a key value pair of username and the list of features they have opted into
00359| 
00360|               Users are GitHub usernames with the @ prefix. Each user is also a comma-separated list of features/experiments to enable.
00361|                   - Example line: "@User1,lf,split_build"
00362|                   - A "#" prefix indicates the user is opted out of all experiments
00363| 
00364| 
00365|               """
00366|               optins = UserOptins()
00367|               for user in user_optin_text.split("\n"):
00368|                   user = user.strip("\r\n\t -")
00369|                   if not user or not user.startswith("@"):
00370|                       # Not a valid user. Skip
00371|                       continue
00372| 
00373|                   if user:
00374|                       usr_name = user.split(",")[0].strip("@")
00375|                       optins[usr_name] = [exp.strip(" ") for exp in user.split(",")[1:]]
00376| 
00377|               return optins
00378| 
00379| 
00380|           def is_valid_experiment_name(experiment_name: str) -> bool:
00381|               """
00382|               Check if the experiment name is valid.
00383|               A valid name:
00384|                   - Contains only alphanumeric characters and the special characters "_" & "-"
00385|                   - The special characters "_" & "-" shouldn't be the first or last characters
00386|                   - Cannot contain spaces
00387|               """
00388| 
00389|               valid_char_regex = r"^[a-zA-Z0-9]([\w-]*[a-zA-Z0-9])?$"
00390|               valid = bool(re.match(valid_char_regex, experiment_name))
00391| 
00392|               if valid:
00393|                   return True
00394| 
00395|               log.error(
00396|                   f"Invalid experiment name: {experiment_name}. Experiment names should only contain alphanumeric characters, '_', and '-'. They cannot contain spaces, and the special characters '_' and '-' cannot be the first or last characters."
00397|               )
00398|               return False
00399| 
00400| 
00401|           def parse_settings_from_text(settings_text: str) -> Settings:
00402|               """
00403|               Parse the experiments from the issue body into a list of ExperimentSettings
00404|               """
00405|               try:
00406|                   if settings_text:
00407|                       # Escape the backtick as well so that we can have the settings in a code block on the GH issue
00408|                       # for easy reading
00409|                       # Note: Using ascii for the backtick so that the cat step in _runner-determinator.yml doesn't choke on
00410|                       #       the backtick character in shell commands.
00411|                       backtick = chr(96)  # backtick character
00412|                       settings_text = settings_text.strip(f"\r\n\t{backtick} ")
00413|                       settings = load_yaml(settings_text)
00414| 
00415|                       # For now we just load experiments. We can expand this if/when we add more settings
00416|                       experiments = {}
00417| 
00418|                       for exp_name, exp_settings in settings.get(SETTING_EXPERIMENTS).items():
00419|                           if not is_valid_experiment_name(exp_name):
00420|                               # Exclude invalid experiments from the list. We log an error, but don't raise an exception so that other experiments can still be processed.
00421|                               continue
00422| 
00423|                           valid_settings = {}
00424|                           for setting in exp_settings:
00425|                               if setting not in Experiment._fields:
00426|                                   log.warning(
00427|                                       f"Unexpected setting in experiment: {setting} = {exp_settings[setting]}"
00428|                                   )
00429|                               else:
00430|                                   valid_settings[setting] = exp_settings[setting]
00431| 
00432|                           experiments[exp_name] = Experiment(**valid_settings)
00433|                       return Settings(experiments)
00434| 
00435|               except Exception:
00436|                   log.exception("Failed to parse settings")
00437| 
00438|               return Settings()
00439| 
00440| 
00441|           def parse_settings(rollout_state: str) -> Settings:
00442|               """
00443|               Parse settings, if any, from the rollout state.
00444| 
00445|               If the issue body contains "---" then the text above that is the settings
00446|               and the text below is the list of opted in users.
00447| 
00448|               If it doesn't contain "---" then the settings are empty and the default values are used.
00449|               """
00450|               settings_text, _ = extract_settings_user_opt_in_from_text(rollout_state)
00451|               return parse_settings_from_text(settings_text)
00452| 
00453| 
00454|           def parse_users(rollout_state: str) -> UserOptins:
00455|               """
00456|               Parse users from the rollout state.
00457| 
00458|               """
00459|               _, users_text = extract_settings_user_opt_in_from_text(rollout_state)
00460|               return parse_user_opt_in_from_text(users_text)
00461| 
00462| 
00463|           def is_user_opted_in(user: str, user_optins: UserOptins, experiment_name: str) -> bool:
00464|               """
00465|               Check if a user is opted into an experiment
00466|               """
00467|               return experiment_name in user_optins.get(user, [])
00468| 
00469| 
00470|           def is_user_opted_out(user: str, user_optins: UserOptins, experiment_name: str) -> bool:
00471|               """
00472|               Check if a user explicitly opted out of an experiment
00473|               """
00474|               # if the experiment is prefixed with a "-", then it's an opt-out
00475|               experiment_optout = "-" + experiment_name
00476|               if experiment_optout not in user_optins.get(user, []):
00477|                   return False
00478| 
00479|               if is_user_opted_in(user, user_optins, experiment_name):
00480|                   log.warning(
00481|                       f"User {user} is opted into experiment {experiment_name}, but also opted out of it. Defaulting to opting out"
00482|                   )
00483| 
00484|               return True
00485| 
00486| 
00487|           def get_runner_prefix(
00488|               rollout_state: str,
00489|               workflow_requestors: Iterable[str],
00490|               branch: str,
00491|               eligible_experiments: FrozenSet[str] = frozenset(),
00492|               is_canary: bool = False,
00493|           ) -> str:
00494|               settings = parse_settings(rollout_state)
00495|               user_optins = parse_users(rollout_state)
00496| 
00497|               fleet_prefix = ""
00498|               prefixes = []
00499|               for experiment_name, experiment_settings in settings.experiments.items():
00500|                   if not experiment_settings.all_branches and is_exception_branch(branch):
00501|                       log.info(
00502|                           f"Branch {branch} is an exception branch. Not enabling experiment {experiment_name}."
00503|                       )
00504|                       continue
00505| 
00506|                   if eligible_experiments:
00507|                       if experiment_name not in eligible_experiments:
00508|                           exp_list = ", ".join(eligible_experiments)
00509|                           log.info(
00510|                               f"Skipping experiment '{experiment_name}', as it is not in the eligible_experiments list: {exp_list}"
00511|                           )
00512|                           continue
00513|                   elif not experiment_settings.default:
00514|                       log.info(
00515|                           f"Skipping experiment '{experiment_name}', as it is not a default experiment"
00516|                       )
00517|                       continue
00518| 
00519|                   # Is any workflow_requestor opted out to this experiment?
00520|                   opted_out_users = [
00521|                       requestor
00522|                       for requestor in workflow_requestors
00523|                       if is_user_opted_out(requestor, user_optins, experiment_name)
00524|                   ]
00525| 
00526|                   if opted_out_users:
00527|                       log.info(
00528|                           f"{', '.join(opted_out_users)} have opted out of experiment {experiment_name}."
00529|                       )
00530|                       continue
00531| 
00532|                   # Is any workflow_requestor opted in to this experiment?
00533|                   opted_in_users = [
00534|                       requestor
00535|                       for requestor in workflow_requestors
00536|                       if is_user_opted_in(requestor, user_optins, experiment_name)
00537|                   ]
00538| 
00539|                   enabled = False
00540|                   if opted_in_users:
00541|                       log.info(
00542|                           f"{', '.join(opted_in_users)} have opted into experiment {experiment_name}."
00543|                       )
00544|                       enabled = True
00545| 
00546|                   elif experiment_settings.rollout_perc:
00547|                       # If no user is opted in, then we randomly enable the experiment based on the rollout percentage
00548|                       if random.uniform(0, 100) <= experiment_settings.rollout_perc:
00549|                           log.info(
00550|                               f"Based on rollout percentage of {experiment_settings.rollout_perc}%, enabling experiment {experiment_name}."
00551|                           )
00552|                           enabled = True
00553| 
00554|                   if enabled:
00555|                       label = experiment_name
00556|                       if experiment_name == LF_FLEET_EXPERIMENT:
00557|                           # We give some special treatment to the "lf" experiment since determines the fleet we use
00558|                           #  - If it's enabled, then we always list it's prefix first
00559|                           #  - If we're in the canary branch, then we append ".c" to the lf prefix
00560|                           if is_canary:
00561|                               label += CANARY_FLEET_SUFFIX
00562|                           fleet_prefix = label
00563|                       else:
00564|                           prefixes.append(label)
00565| 
00566|               if len(prefixes) > 1:
00567|                   log.error(
00568|                       f"Only a fleet and one other experiment can be enabled for a job at any time. Enabling {prefixes[0]} and ignoring the rest, which are {', '.join(prefixes[1:])}"
00569|                   )
00570|                   prefixes = prefixes[:1]
00571| 
00572|               # Fleet always comes first
00573|               if fleet_prefix:
00574|                   prefixes.insert(0, fleet_prefix)
00575| 
00576|               return ".".join(prefixes) + "." if prefixes else ""
00577| 
00578| 
00579|           def get_rollout_state_from_issue(github_token: str, repo: str, issue_num: int) -> str:
00580|               """
00581|               Gets the first comment of the issue, which contains the desired rollout state.
00582| 
00583|               The default issue we use - https://github.com/pytorch/test-infra/issues/5132
00584|               """
00585|               gh = get_gh_client(github_token)
00586|               issue = get_issue(gh, repo, issue_num)
00587|               return str(issue.get_comments()[0].body.strip("\n\t "))
00588| 
00589| 
00590|           def download_json(url: str, headers: Dict[str, str], num_retries: int = 3) -> Any:
00591|               for _ in range(num_retries):
00592|                   try:
00593|                       req = Request(url=url, headers=headers)
00594|                       content = urlopen(req, timeout=5).read().decode("utf-8")
00595|                       return json.loads(content)
00596|                   except Exception as e:
00597|                       log.warning(f"Could not download {url}: {e}")
00598| 
00599|               log.warning(f"All {num_retries} retries exhausted, downloading {url} failed")
00600|               return {}
00601| 
00602| 
00603|           @lru_cache(maxsize=None)
00604|           def get_pr_info(github_repo: str, github_token: str, pr_number: int) -> Dict[str, Any]:
00605|               """
00606|               Dynamically get PR information
00607|               """
00608|               github_api = f"https://api.github.com/repos/{github_repo}"
00609|               headers = {
00610|                   "Accept": "application/vnd.github.v3+json",
00611|                   "Authorization": f"token {github_token}",
00612|               }
00613|               json_response: Dict[str, Any] = download_json(
00614|                   url=f"{github_api}/issues/{pr_number}",
00615|                   headers=headers,
00616|               )
00617| 
00618|               if not json_response:
00619|                   log.warning(f"Failed to get the labels for #{pr_number}")
00620|                   return {}
00621| 
00622|               return json_response
00623| 
00624| 
00625|           def get_labels(github_repo: str, github_token: str, pr_number: int) -> Set[str]:
00626|               """
00627|               Dynamically get the latest list of labels from the pull request
00628|               """
00629|               pr_info = get_pr_info(github_repo, github_token, pr_number)
00630|               return {
00631|                   label.get("name") for label in pr_info.get("labels", []) if label.get("name")
00632|               }
00633| 
00634| 
00635|           def main() -> None:
00636|               args = parse_args()
00637| 
00638|               runner_label_prefix = DEFAULT_LABEL_PREFIX
00639| 
00640|               # Check if the PR is opt-out
00641|               if args.pr_number:
00642|                   labels = get_labels(args.github_repo, args.github_token, int(args.pr_number))
00643|                   if OPT_OUT_LABEL in labels:
00644|                       log.info(
00645|                           f"Opt-out runner determinator because #{args.pr_number} has {OPT_OUT_LABEL} label"
00646|                       )
00647|                       set_github_output(GH_OUTPUT_KEY_LABEL_TYPE, runner_label_prefix)
00648|                       sys.exit()
00649| 
00650|               try:
00651|                   rollout_state = get_rollout_state_from_issue(
00652|                       args.github_token, args.github_issue_repo, args.github_issue
00653|                   )
00654| 
00655|                   username = get_potential_pr_author(
00656|                       args.github_token,
00657|                       args.github_repo,
00658|                       args.github_actor,
00659|                       args.github_ref_type,
00660|                       args.github_branch,
00661|                   )
00662| 
00663|                   is_canary = args.github_repo == "pytorch/pytorch-canary"
00664| 
00665|                   runner_label_prefix = get_runner_prefix(
00666|                       rollout_state,
00667|                       (args.github_issue_owner, username),
00668|                       args.github_branch,
00669|                       args.eligible_experiments,
00670|                       is_canary,
00671|                   )
00672| 
00673|               except Exception as e:
00674|                   log.error(
00675|                       f"Failed to get issue. Defaulting to Meta runners and no experiments. Exception: {e}"
00676|                   )
00677| 
00678|               set_github_output(GH_OUTPUT_KEY_LABEL_TYPE, runner_label_prefix)
00679| 
00680| 
00681|           if __name__ == "__main__":
00682|               main()
00683| 
00684|           EOF
00685| 
00686|           cat runner_determinator.py
00687| 
00688|       - name: Install dependencies
00689|         run: python3 -m pip install urllib3==1.26.18 PyGithub==2.3.0
00690| 
00691|       - name: Get the workflow type for the current user
00692|         id: set-condition
00693|         run: |
00694|           curr_branch="${{ inputs.curr_branch }}"
00695|           curr_ref_type="${{ inputs.curr_ref_type }}"
00696|           echo "Current branch is '$curr_branch'"
00697| 
00698|           python3 runner_determinator.py \
00699|             --github-token "$GITHUB_TOKEN" \
00700|             --github-issue "$ISSUE_NUMBER" \
00701|             --github-branch "$curr_branch" \
00702|             --github-actor "$TRIGGERING_ACTOR" \
00703|             --github-issue-owner "$ISSUE_OWNER" \
00704|             --github-ref-type "$curr_ref_type" \
00705|             --github-repo "$GITHUB_REPOSITORY" \
00706|             --eligible-experiments "$CHECK_EXPERIMENTS" \
00707|             --pr-number "${PR_NUMBER}"
00708| 

(End of file - total 708 lines)
</file>
```

---

## Assistant (Build · openrouter/pony-alpha · 249.9s)

_Thinking:_

Now I have a comprehensive view of the PyTorch CI/CD system. Let me create a more detailed and complete architecture diagram that includes all the job types, workflows, and their relationships.

Now I have comprehensive information. Here's the **complete PyTorch CI/CD Architecture**:

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           PYTORCH CI/CD ARCHITECTURE (v2.6)                              │
└─────────────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                              TRIGGER SOURCES                                             │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│  • pull_request → PRs to main, release/*, landchecks/*                                  │
│  • push         → Commits to main, release/*, nightly                                   │
│  • schedule     → Cron jobs (periodic, nightly, slow tests)                             │
│  • tags         → ciflow/trunk/*, ciflow/periodic/*, ciflow/inductor/*, etc.            │
│  • workflow_dispatch → Manual triggers                                                  │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           MAIN ENTRY WORKFLOWS                                           │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  ┌─────────────────┐  │
│  │    pull.yml      │  │    trunk.yml     │  │  periodic.yml    │  │    lint.yml     │  │
│  │ (PR validation)  │  │ (post-merge CI)  │  │ (scheduled CI)   │  │   (code lint)   │  │
│  │                  │  │                  │  │                  │  │                 │  │
│  │ Triggers: PR/push│  │ Triggers: push   │  │ Triggers: cron   │  │ Triggers: PR    │  │
│  │ to main/release  │  │ to main/release  │  │ every 4-8hrs     │  │                 │  │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘  └────────┬────────┘  │
│           │                     │                     │                     │            │
│  ┌────────┴─────────┐  ┌────────┴─────────┐  ┌────────┴─────────┐  ┌────────┴────────┐  │
│  │    slow.yml      │  │  inductor.yml    │  │inductor-periodic │  │  torchbench.yml │  │
│  │ (slow tests)     │  │ (inductor bench) │  │.yml              │  │ (benchmark)     │  │
│  │                  │  │                  │  │(periodic ind.)   │  │                 │  │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘  └─────────────────┘  │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                        PRE-BUILD PHASE (Orchestration)                                   │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  ┌──────────────────────────────────┐    ┌───────────────────────────────────────────┐  │
│  │   _runner-determinator.yml       │    │        llm_td_retrieval.yml               │  │
│  │                                  │    │                                           │  │
│  │  Determines runner fleet:        │    │   LLM-based test selection:               │  │
│  │  • "" (default/Meta runners)     │    │   • Analyzes code changes                │  │
│  │  • "lf." (Linux Foundation)      │    │   • Selects relevant test targets        │  │
│  │  • "lf.c." (LF Canary)           │    │   • Reduces unnecessary test runs        │  │
│  │                                  │    │                                           │  │
│  │  Output: label-type prefix       │    └──────────────────┬────────────────────────┘  │
│  └──────────────────────────────────┘                       │                           │
│                                           ┌──────────────────┴────────────────────────┐  │
│                                           │      target_determination.yml            │  │
│                                           │                                          │  │
│                                           │  • Downloads TD artifacts               │  │
│                                           │  • Calculates which tests to run        │  │
│                                           │  • Passes test selection to build jobs  │  │
│                                           └──────────────────────────────────────────┘  │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                      BUILD JOBS (Platform Matrix)                                        │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  ╔═══════════════════════════════════════════════════════════════════════════════════╗  │
│  ║                           LINUX BUILDS (_linux-build.yml)                          ║  │
│  ╠═══════════════════════════════════════════════════════════════════════════════════╣  │
│  ║                                                                                    ║  │
│  ║  CPU ONLY:                                                                         ║  │
│  ║  ┌─────────────────────────────────────────────────────────────────────────────┐  ║  │
│  ║  │ linux-jammy-py3.9-gcc11           - Ubuntu 22.04, Python 3.9, GCC 11       │  ║  │
│  ║  │ linux-jammy-py3.9-gcc11-no-ops    - No per-operator headers build          │  ║  │
│  ║  │ linux-jammy-py3.9-gcc11-pch       - Precompiled headers build              │  ║  │
│  ║  │ linux-jammy-py3.10-clang15-asan   - Address Sanitizer build                │  ║  │
│  ║  │ linux-focal-py3.9-clang10         - Ubuntu 20.04, Python 3.9, Clang 10     │  ║  │
│  ║  │ linux-focal-py3.11-clang10        - Ubuntu 20.04, Python 3.11, Clang 10    │  ║  │
│  ║  │ linux-focal-py3.12-clang10        - Ubuntu 20.04, Python 3.12, Clang 10    │  ║  │
│  ║  │ linux-focal-py3.13-clang10        - Ubuntu 20.04, Python 3.13, Clang 10    │  ║  │
│  ║  │ linux-focal-py3.9-clang10-onnx    - ONNX build variant                     │  ║  │
│  ║  │ linux-focal-cpu-py3.10-gcc9-bazel - Bazel build system test               │  ║  │
│  ║  └─────────────────────────────────────────────────────────────────────────────┘  ║  │
│  ║                                                                                    ║  │
│  ║  NVIDIA CUDA:                                                                      ║  │
│  ║  ┌─────────────────────────────────────────────────────────────────────────────┐  ║  │
│  ║  │ linux-focal-cuda11.8-py3.10-gcc9  - CUDA 11.8, cuDNN 9                    │  ║  │
│  ║  │ linux-focal-cuda12.1-py3.10-gcc9  - CUDA 12.1, cuDNN 9                    │  ║  │
│  ║  │ linux-focal-cuda12.4-py3.10-gcc9  - CUDA 12.4, cuDNN 9                    │  ║  │
│  ║  │ linux-focal-cuda12.4-py3.10-gcc9-sm89 - SM89 (Ada) architecture            │  ║  │
│  ║  │ linux-jammy-cuda11.8-cudnn9-py3.9-clang12 - CUDA with Clang               │  ║  │
│  ║  └─────────────────────────────────────────────────────────────────────────────┘  ║  │
│  ║                                                                                    ║  │
│  ║  AMD ROCm:                                                                         ║  │
│  ║  ┌─────────────────────────────────────────────────────────────────────────────┐  ║  │
│  ║  │ linux-focal-rocm6.2-py3.10  - ROCm 6.2, AMD GPU support                    │  ║  │
│  ║  └─────────────────────────────────────────────────────────────────────────────┘  ║  │
│  ║                                                                                    ║  │
│  ║  Specialized:                                                                      ║  │
│  ║  ┌─────────────────────────────────────────────────────────────────────────────┐  ║  │
│  ║  │ linux-focal-py3.9-clang9-xla           - XLA/TPU build                     │  ║  │
│  ║  │ linux-jammy-py3-clang12-executorch     - ExecuTorch build                  │  ║  │
│  ║  │ linux-jammy-py3-clang12-mobile         - Mobile build                      │  ║  │
│  ║  │ linux-jammy-py3.9-gcc11-mobile-lightweight-dispatch - Mobile LD            │  ║  │
│  ║  │ libtorch-linux-focal-cuda12.*-debug    - Libtorch debug builds             │  ║  │
│  ║  └─────────────────────────────────────────────────────────────────────────────┘  ║  │
│  ╚═══════════════════════════════════════════════════════════════════════════════════╝  │
│                                                                                          │
│  ╔═══════════════════════════════════════════════════════════════════════════════════╗  │
│  ║                          MACOS BUILDS (_mac-build.yml)                             ║  │
│  ╠═══════════════════════════════════════════════════════════════════════════════════╣  │
│  ║  ┌─────────────────────────────────────────────────────────────────────────────┐  ║  │
│  ║  │ macos-py3-arm64  - macOS M1/M2, Python 3.9, ARM64                         │  ║  │
│  ║  └─────────────────────────────────────────────────────────────────────────────┘  ║  │
│  ╚═══════════════════════════════════════════════════════════════════════════════════╝  │
│                                                                                          │
│  ╔═══════════════════════════════════════════════════════════════════════════════════╗  │
│  ║                         WINDOWS BUILDS (_win-build.yml)                            ║  │
│  ╠═══════════════════════════════════════════════════════════════════════════════════╣  │
│  ║  ┌─────────────────────────────────────────────────────────────────────────────┐  ║  │
│  ║  │ win-vs2019-cpu-py3     - Windows Server 2019, VS2019, CPU only             │  ║  │
│  ║  │ win-vs2019-cuda12.1-py3 - Windows Server 2019, VS2019, CUDA 12.1           │  ║  │
│  ║  └─────────────────────────────────────────────────────────────────────────────┘  ║  │
│  ╚═══════════════════════════════════════════════════════════════════════════════════╝  │
│                                                                                          │
│  ╔═══════════════════════════════════════════════════════════════════════════════════╗  │
│  ║                        BAZEL BUILD (_bazel-build-test.yml)                         ║  │
│  ╠═══════════════════════════════════════════════════════════════════════════════════╣  │
│  ║  ┌─────────────────────────────────────────────────────────────────────────────┐  ║  │
│  ║  │ linux-focal-cuda12.4-py3.10-gcc9-bazel - Bazel build with CUDA             │  ║  │
│  ║  │ linux-focal-cpu-py3.10-gcc9-bazel        - Bazel build CPU only             │  ║  │
│  ║  └─────────────────────────────────────────────────────────────────────────────┘  ║  │
│  ╚═══════════════════════════════════════════════════════════════════════════════════╝  │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                         TEST CONFIGURATIONS (Sharded)                                    │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐  │
│  │                        CORE TEST CONFIGS                                           │  │
│  ├───────────────────────────────────────────────────────────────────────────────────┤  │
│  │ config: "default"           - Standard PyTorch tests (sharded 5 ways)             │  │
│  │ config: "distributed"       - Distributed training tests (sharded 2-3 ways)       │  │
│  │ config: "jit_legacy"        - Legacy JIT compiler tests                           │  │
│  │ config: "crossref"          - Cross-reference tests                               │  │
│  │ config: "dynamo_wrapped"    - TorchDynamo wrapped tests (sharded 3 ways)          │  │
│  │ config: "docs_test"         - Documentation building tests                        │  │
│  │ config: "backwards_compat"  - Backward compatibility tests                        │  │
│  │ config: "numpy_2_x"         - NumPy 2.x compatibility tests                       │  │
│  │ config: "nogpu_AVX512"      - CPU-only AVX512 tests                               │  │
│  │ config: "nogpu_NO_AVX2"     - CPU-only non-AVX2 tests                             │  │
│  │ config: "multigpu"          - Multi-GPU tests                                     │  │
│  └───────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                          │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐  │
│  │                        INDUCTOR TEST CONFIGS                                       │  │
│  ├───────────────────────────────────────────────────────────────────────────────────┤  │
│  │ config: "inductor"                    - Core inductor unit tests                  │  │
│  │ config: "inductor_distributed"        - Inductor distributed tests                │  │
│  │ config: "inductor_cpp_wrapper"        - C++ wrapper tests                         │  │
│  │ config: "inductor_huggingface"        - HuggingFace model benchmarks              │  │
│  │ config: "inductor_timm"               - Timm model benchmarks                     │  │
│  │ config: "inductor_torchbench"         - TorchBench benchmarks                     │  │
│  │ config: "inductor_amx"                - AMX SIMD tests                            │  │
│  │ config: "inductor_avx2"               - AVX2 SIMD tests                           │  │
│  │ config: "inductor-halide"             - Halide backend tests                      │  │
│  │ config: "inductor-triton-cpu"         - Triton CPU tests                         │  │
│  │ config: "cpu_inductor_*"              - CPU inductor variants                     │  │
│  │ config: "dynamic_*"                   - Dynamic shape tests                       │  │
│  │ config: "aot_*"                       - Ahead-of-time compilation tests           │  │
│  └───────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                          │
│  ┌───────────────────────────────────────────────────────────────────────────────────┐  │
│  │                        SPECIALIZED TEST CONFIGS                                    │  │
│  ├───────────────────────────────────────────────────────────────────────────────────┤  │
│  │ config: "slow"              - Slow-running tests (periodic only)                  │  │
│  │ config: "mem_leak_check"    - Memory leak detection tests                        │  │
│  │ config: "rerun_disabled_tests" - Re-run previously disabled tests                │  │
│  │ config: "pr_time_benchmarks" - PR timing benchmarks                               │  │
│  │ config: "xla"               - XLA/TPU tests                                       │  │
│  │ config: "executorch"        - ExecuTorch tests                                    │  │
│  │ config: "mps"               - Metal Performance Shaders (macOS)                   │  │
│  │ config: "torchbench_*"      - TorchBench performance tests                       │  │
│  │ config: "dynamo_eager_*"    - Dynamo eager mode benchmarks                       │  │
│  │ config: "aot_eager_*"       - AOT eager mode benchmarks                          │  │
│  └───────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                         TEST WORKFLOWS (Reusable)                                        │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  ┌─────────────────┐  │
│  │ _linux-test.yml  │  │  _mac-test.yml   │  │  _win-test.yml   │  │ _rocm-test.yml  │  │
│  │                  │  │                  │  │                  │  │                 │  │
│  │ • Matrix testing │  │ • macOS testing  │  │ • Windows tests  │  │ • AMD GPU tests │  │
│  │ • Docker-based   │  │ • ARM64 native   │  │ • VS2019 env     │  │ • ROCm stack    │  │
│  │ • GPU/CPU runners│  │                  │  │                  │  │                 │  │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘  └─────────────────┘  │
│                                                                                          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐                        │
│  │_mac-test-mps.yml │  │  _xpu-test.yml   │  │     _docs.yml    │                        │
│  │                  │  │                  │  │                  │                        │
│  │ • Metal shaders  │  │ • Intel XPU      │  │ • Doc building   │                        │
│  │ • macOS 13/14    │  │ • Intel GPUs     │  │ • Sphinx         │                        │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘                        │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                         COMPOSITE ACTIONS (.github/actions/)                             │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  SETUP/TEARDOWN:              ARTIFACTS:                 TESTING:                        │
│  ┌─────────────────────┐     ┌─────────────────────┐    ┌─────────────────────┐         │
│  │ setup-linux         │     │ download-build-     │    │ filter-test-configs │         │
│  │ setup-win           │     │   artifacts         │    │ linux-test          │         │
│  │ setup-rocm          │     │ upload-test-        │    │ test-pytorch-binary │         │
│  │ setup-xpu           │     │   artifacts         │    │ pytest-cache-       │         │
│  │ teardown-rocm       │     │ download-td-        │    │   download          │         │
│  │ teardown-win        │     │   artifacts         │    │ pytest-cache-       │         │
│  │ teardown-xpu        │     │ upload-sccache-     │    │   upload            │         │
│  │ diskspace-cleanup   │     │   stats             │    │                     │         │
│  └─────────────────────┘     └─────────────────────┘    └─────────────────────┘         │
│                                                                                          │
│  UTILITIES:                                                                              │
│  ┌─────────────────────┐     ┌─────────────────────┐    ┌─────────────────────┐         │
│  │ checkout-pytorch    │     │ get-workflow-job-id │    │ chown-workspace     │         │
│  │ build-android       │     │                     │    │                     │         │
│  └─────────────────────┘     └─────────────────────┘    └─────────────────────┘         │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                         TEST EXECUTION (.ci/pytorch/)                                    │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐  ┌────────────────────┐    │
│  │   build.sh     │  │   test.sh      │  │multigpu-test.sh│  │   docs-test.sh     │    │
│  │                │  │                │  │                │  │                    │    │
│  │ • cmake config │  │ • pytest run   │  │ • multi-GPU    │  │ • Sphinx build     │    │
│  │ • ninja build  │  │ • sharding     │  │ • distributed  │  │ • Doc validation   │    │
│  │ • wheel create │  │ • TD selection │  │ • NCCL tests   │  │                    │    │
│  └────────────────┘  └────────────────┘  └────────────────┘  └────────────────────┘    │
│                                                                                          │
│  Environment Variables:                                                                  │
│  • SHARD_NUMBER / NUM_TEST_SHARDS  - Test parallelization                              │
│  • TEST_CONFIG                     - Test configuration type                           │
│  • BUILD_ENVIRONMENT               - Build identifier                                  │
│  • TORCH_CUDA_ARCH_LIST            - CUDA architectures                                │
│  • SCCACHE_*                       - Distributed compilation cache                     │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                    BINARY BUILD WORKFLOWS (Generated from Templates)                     │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  Templates: .github/templates/*.j2  →  Generated: .github/workflows/generated-*.yml     │
│                                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────────────────┐    │
│  │                     LINUX BINARIES                                               │    │
│  ├─────────────────────────────────────────────────────────────────────────────────┤    │
│  │ generated-linux-binary-manywheel-nightly.yml                                     │    │
│  │   • manywheel-py3.9-cpu         • manywheel-py3.10-cuda11.8                    │    │
│  │   • manywheel-py3.10-cpu        • manywheel-py3.10-cuda12.1                    │    │
│  │   • manywheel-py3.11-cpu        • manywheel-py3.10-cuda12.4                    │    │
│  │   • manywheel-py3.12-cpu        • manywheel-py3.11-cuda12.4                    │    │
│  │                                                                                 │    │
│  │ generated-linux-binary-libtorch-cxx11-abi-nightly.yml                           │    │
│  │ generated-linux-binary-libtorch-pre-cxx11-nightly.yml                           │    │
│  │ generated-linux-aarch64-binary-manywheel-nightly.yml (ARM64)                    │    │
│  │ generated-linux-s390x-binary-manywheel-nightly.yml (s390x)                      │    │
│  └─────────────────────────────────────────────────────────────────────────────────┘    │
│                                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────────────────┐    │
│  │                     MACOS BINARIES                                               │    │
│  ├─────────────────────────────────────────────────────────────────────────────────┤    │
│  │ generated-macos-arm64-binary-wheel-nightly.yml                                  │    │
│  │ generated-macos-arm64-binary-libtorch-cxx11-abi-nightly.yml                     │    │
│  └─────────────────────────────────────────────────────────────────────────────────┘    │
│                                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────────────────┐    │
│  │                     WINDOWS BINARIES                                             │    │
│  ├─────────────────────────────────────────────────────────────────────────────────┤    │
│  │ generated-windows-binary-wheel-nightly.yml                                       │    │
│  │   • py3.9-cpu, py3.10-cpu, py3.11-cpu, py3.12-cpu                              │    │
│  │   • py3.10-cuda11.8, py3.10-cuda12.1, py3.10-cuda12.4                          │    │
│  │                                                                                 │    │
│  │ generated-windows-binary-libtorch-debug-nightly.yml                             │    │
│  │ generated-windows-binary-libtorch-release-nightly.yml                           │    │
│  └─────────────────────────────────────────────────────────────────────────────────┘    │
│                                                                                          │
│  Binary workflow uses: _binary-build-linux.yml, _binary-test-linux.yml, _binary-upload │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                         RUNNER TYPES (Self-Hosted)                                       │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                          │
│  ┌─────────────────────── LINUX ───────────────────────┐    ┌────── MACOS ──────┐      │
│  │ linux.2xlarge         - 8 vCPU, 32GB RAM            │    │ macos-m1-stable   │      │
│  │ linux.4xlarge         - 16 vCPU, 64GB RAM           │    │ macos-m1-13       │      │
│  │ linux.8xlarge.amx     - AMX SIMD support            │    │ macos-m1-14       │      │
│  │ linux.10xlarge.avx2   - AVX2 SIMD support           │    └───────────────────┘      │
│  │ linux.12xlarge        - High memory                 │                               │
│  │ linux.24xl.spr-metal  - Sapphire Rapids             │    ┌────── WINDOWS ────┐      │
│  │ linux.g4dn.12xlarge.nvidia.gpu - T4 GPU (4x)        │    │ windows.4xlarge.  │      │
│  │ linux.g5.4xlarge.nvidia.gpu  - A10G GPU             │    │   nonephemeral    │      │
│  │ linux.g5.12xlarge.nvidia.gpu - A10G GPU (4x)        │    └───────────────────┘      │
│  │ linux.g6.4xlarge.experimental.nvidia.gpu - L4 GPU   │                               │
│  │ linux.gcp.a100        - A100 40GB (Google Cloud)    │    ┌────── ROCm ───────┐      │
│  │ linux.rocm.gpu        - AMD ROCm GPU                │    │ linux.rocm.gpu    │      │
│  └──────────────────────────────────────────────────────┘    └───────────────────┘      │
│                                                                                          │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

## Complete Job List by Workflow

### pull.yml (PR CI)
| Job Name | Platform | Description |
|----------|----------|-------------|
| `linux-jammy-py3_9-gcc11-build/test` | Linux CPU | Main CPU build with GCC 11 |
| `linux-jammy-py3_9-gcc11-no-ops` | Linux CPU | No per-operator headers |
| `linux-jammy-py3_9-gcc11-pch` | Linux CPU | Precompiled headers |
| `linux-jammy-py3_10-clang15-asan-build/test` | Linux CPU | Address Sanitizer |
| `linux-focal-py3_9-clang10-build/test` | Linux CPU | Clang 10, Python 3.9 |
| `linux-focal-py3_11-clang10-build/test` | Linux CPU | Clang 10, Python 3.11 |
| `linux-focal-py3_12-clang10-build/test` | Linux CPU | Clang 10, Python 3.12 |
| `linux-focal-py3_13-clang10-build/test` | Linux CPU | Clang 10, Python 3.13 |
| `linux-focal-py3_9-clang10-onnx-build/test` | Linux CPU | ONNX variant |
| `linux-focal-cuda11_8-py3_10-gcc9-build/test` | Linux GPU | CUDA 11.8 distributed |
| `linux-focal-cuda12_4-py3_10-gcc9-build/test` | Linux GPU | CUDA 12.4 |
| `linux-focal-cuda12_4-py3_10-gcc9-sm89-build/test` | Linux GPU | SM89 (Ada) |
| `linux-focal-cpu-py3_10-gcc9-bazel-test` | Linux CPU | Bazel build |
| `linux-focal-py3_9-clang9-xla-build/test` | Linux CPU | XLA/TPU |
| `linux-focal-rocm6_2-py3_10-build` | Linux ROCm | AMD GPU |
| `linux-jammy-py3-clang12-executorch-build/test` | Linux CPU | ExecuTorch |
| `linux-jammy-py3-clang12-mobile-build` | Linux CPU | Mobile |
| `win-vs2019-cpu-py3-build/test` | Windows | CPU build |
| `linux-docs` | Linux CPU | Documentation |

### trunk.yml (Post-merge)
| Job Name | Platform | Description |
|----------|----------|-------------|
| `libtorch-linux-focal-cuda12.1-py3.7-gcc9-debug-build` | Linux GPU | Libtorch debug |
| `libtorch-linux-focal-cuda12.4-py3.7-gcc9-debug-build` | Linux GPU | Libtorch debug |
| `linux-focal-cuda12.1-py3.10-gcc9-no-ops-build` | Linux GPU | No-ops build |
| `linux-focal-cuda12.4-py3.10-gcc9-no-ops-build` | Linux GPU | No-ops build |
| `macos-py3-arm64-build/test` | macOS | M1/M2 ARM64 |
| `macos-py3-arm64-mps-test` | macOS | Metal Performance Shaders |
| `win-vs2019-cuda12.1-py3-build` | Windows | CUDA 12.1 |
| `linux-focal-rocm6_2-py3_10-build/test` | Linux ROCm | AMD GPU |

### inductor.yml / inductor-unittest.yml
| Job Name | Config | Description |
|----------|--------|-------------|
| `linux-focal-cuda12.4-py3.10-gcc9-inductor-build/test` | inductor | GPU inductor unit tests |
| `linux-focal-cuda12.4-py3.12-gcc9-inductor-build/test` | inductor | Python 3.12 variant |
| `linux-focal-cuda12.4-py3.13-gcc9-inductor-build/test` | inductor | Python 3.13 variant |
| `linux-jammy-cpu-py3.9-gcc11-inductor-build/test` | inductor_amx/avx2 | CPU SIMD tests |
| `linux-jammy-cpu-py3.12-inductor-halide-build/test` | inductor-halide | Halide backend |
| `linux-jammy-cpu-py3.12-inductor-triton-cpu-build/test` | inductor-triton-cpu | Triton CPU |

### slow.yml
| Job Name | Config | Description |
|----------|--------|-------------|
| `linux-focal-cuda12.1-py3.10-gcc9-sm86-build/test` | slow | Slow GPU tests |
| `linux-focal-py3.9-clang10-build/test` | slow | Slow CPU tests |
| `linux-focal-rocm6_2-py3_10-build/test` | slow | Slow ROCm tests |
| `linux-jammy-py3_10-clang15-asan-build/test` | slow | Slow ASAN tests |

### periodic.yml
| Job Name | Config | Description |
|----------|--------|-------------|
| `linux-focal-cuda12.1-py3.10-gcc9-build/test` | default/nogpu | Full periodic suite |
| `linux-focal-cuda12.4-py3.10-gcc9-build/test` | default/nogpu | Full periodic suite |
| `linux-focal-cuda11.8-py3.9-gcc9-build/test` | multigpu | Multi-GPU tests |
| `linux-focal-cuda11.8-py3.10-gcc9-debug-build/test` | default | Debug build tests |
| `linux-focal-cuda12.1-py3-gcc9-slow-gradcheck-build/test` | default | Slow gradient check |
| `linux-focal-cuda12.4-py3.10-gcc9-bazel-test` | default | Bazel periodic |
| `linux-focal-rocm6_2-py3_10-build/test` | distributed | ROCm periodic |

### lint.yml
| Job Name | Description |
|----------|-------------|
| `lintrunner-clang` | Clang tidy/format checks |
| `lintrunner-noclang` | Python/other lints |
| `quick-checks` | Non-breaking spaces, file names, shebangs |
| `pr-sanity-checks` | PR size validation |
| `workflow-checks` | Workflow regeneration check |
| `toc` | Table of contents validation |
| `test-tools` | Tools directory tests |
| `test_run_test` | run_test.py usability |
| `test_collect_env` | collect_env.py tests |

---



