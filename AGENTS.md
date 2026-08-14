# AGENTS.md

## Project overview

This repository contains a beginner-friendly Python project for a wheel-leg robot. The intended hardware includes a Raspberry Pi, DC motor drivers, and an MPU6050 IMU. Keep changes small, understandable, and safe for physical hardware.

## Development guidelines

- Use Python 3 and follow PEP 8 unless existing project conventions require otherwise.
- Preserve the public behavior of existing classes and motion-mode names unless the task explicitly requests a breaking change.
- Keep comments and user-facing documentation beginner-friendly. Chinese or bilingual explanations are welcome where they improve clarity.
- Prefer small, focused modules and descriptive names over clever abstractions.
- Do not add dependencies unless they are necessary and documented in `requirements.txt`.
- Never commit secrets, tokens, Wi-Fi credentials, hardware serial numbers, or machine-specific paths.

## Hardware safety

- Treat `stop` as the fail-safe state.
- Validate motion modes, speed ranges, durations, and sensor inputs before sending commands to hardware.
- On invalid input, exceptions, timeouts, or lost sensor data, avoid issuing motion commands and transition to a safe stopped state where appropriate.
- Avoid unexpected motor activation during imports, object construction, tests, or dry runs.
- Keep GPIO, I2C, motor-driver, and sensor access behind replaceable interfaces so logic can be tested without physical hardware.
- Document any behavior that could move hardware before implementation or review.

## Setup and validation

Hardware-specific packages in `requirements.txt` may require a compatible Raspberry Pi environment. Do not assume GPIO or I2C devices exist in cloud development or CI.

Run the checks that are applicable to the change:

```bash
python -m compileall -q .
```

If a `tests/` directory exists:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

When adding tests:

- Mock hardware interfaces and time-dependent behavior.
- Avoid real `time.sleep` calls.
- Cover speed clamping, valid and invalid modes, mode transitions, sequence execution, and emergency stop behavior.
- Keep tests deterministic and runnable without Raspberry Pi hardware.

## Documentation

- Update `README.md` when setup steps, supported hardware, dependencies, motion modes, or user-facing behavior change.
- Include concise examples for new public functionality.
- Clearly separate commands intended for a general development machine from commands that must run on Raspberry Pi hardware.

## Code Review Rules

### Motion safety

- Flag changes that can leave motors active after an error, timeout, invalid command, or explicit stop request.
- Flag changes that bypass validation for motion mode, speed, duration, or sensor-derived control inputs.
- Require the safe default to remain stopped unless the requested behavior explicitly says otherwise.

### Hardware isolation

- Flag tests or module imports that directly activate GPIO, I2C, motors, or sensors.
- Flag hardware-dependent tests that cannot run with mocks or fakes.
- Flag blocking delays in unit tests or control paths where they can prevent timely stop handling.

### Compatibility and quality

- Flag unrequested breaking changes to motion-mode names, command dictionaries, or public method behavior.
- Flag new dependencies that are unused, undocumented, or unsuitable for the supported Raspberry Pi environment.
- Leave formatting and other deterministic style checks to automated tooling unless they conceal a functional defect.
