# Calculator Application

## Overview
A modular Python calculator application demonstrating clean architecture and design patterns.

## Current Architecture

### Components

#### 1. Calculator Class (`main.py`)
**Responsibility**: Core calculation logic
- Handles basic arithmetic operations (+, -, *, /)
- Implements error handling for division by zero
- Returns appropriate error messages for invalid operations

#### 2. InputSystem Class (`input.py`)
**Responsibility**: User input validation and management
- **Design Pattern**: Singleton Pattern
- Ensures single instance across the application
- Validates numeric inputs with retry logic
- Validates operator inputs against allowed operations
- Provides consistent error messaging

#### 3. Main Application (`main.py`)
**Responsibility**: Application orchestration and user interface
- Integrates Calculator and InputSystem components
- Manages application flow and user interaction loop
- Handles graceful exit and error recovery
- Provides clear user feedback and formatting

### Design Patterns Used

1. **Singleton Pattern** (InputSystem)
   - Ensures consistent input handling across the application
   - Prevents multiple instances of input validation logic

2. **Separation of Concerns**
   - Calculator: Pure calculation logic
   - InputSystem: Input validation and user interaction
   - Main: Application flow control

3. **Error Handling Strategy**
   - Defensive programming with try-catch blocks
   - User-friendly error messages
   - Graceful degradation and recovery

## Architecture Diagram

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Main Loop     │    │   InputSystem    │    │   Calculator    │
│   (main.py)     │◄──►│   (input.py)     │    │   (main.py)     │
│                 │    │   [Singleton]    │    │                 │
│ - User Interface│    │ - Input Valid.   │    │ - Arithmetic    │
│ - Flow Control  │    │ - Error Handling │    │ - Operations    │
│ - Integration   │    │ - Retry Logic    │    │ - Error Checks  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## Agile Improvement Roadmap

### Sprint 1: Foundation Enhancement
**Epic**: Core Functionality Improvements

#### User Stories:
- **As a user**, I want to see calculation history so I can review previous operations
- **As a user**, I want to use parentheses in expressions so I can control operation order
- **As a developer**, I want comprehensive unit tests so I can ensure code reliability

#### Technical Tasks:
- [ ] Implement `HistoryManager` class for calculation storage
- [ ] Add expression parser for complex calculations
- [ ] Create comprehensive test suite (pytest)
- [ ] Add logging functionality for debugging

### Sprint 2: User Experience Enhancement
**Epic**: Interface and Usability Improvements

#### User Stories:
- **As a user**, I want keyboard shortcuts so I can operate the calculator efficiently
- **As a user**, I want to save/load calculation sessions so I can resume work
- **As a user**, I want different number format options so I can work in various contexts

#### Technical Tasks:
- [ ] Implement `SessionManager` for save/load functionality
- [ ] Add `NumberFormatter` for different display formats (scientific, engineering)
- [ ] Create `KeyboardHandler` for shortcut management
- [ ] Implement configuration system for user preferences

### Sprint 3: Advanced Features
**Epic**: Mathematical Function Extension

#### User Stories:
- **As a user**, I want scientific functions so I can perform advanced calculations
- **As a user**, I want variable support so I can store and reuse values
- **As a user**, I want graphing capabilities so I can visualize functions

#### Technical Tasks:
- [ ] Implement `ScientificCalculator` extending base Calculator
- [ ] Create `VariableManager` for variable storage and manipulation
- [ ] Add `FunctionLibrary` for mathematical functions
- [ ] Implement basic plotting functionality

## Proposed Architecture Improvements

### 1. Plugin Architecture
```python
class CalculatorPlugin:
    def get_operations(self) -> Dict[str, Callable]
    def get_name(self) -> str
```

### 2. Command Pattern Implementation
```python
class CalculationCommand:
    def execute(self) -> float
    def undo(self) -> None
    def get_description(self) -> str
```

### 3. Observer Pattern for UI Updates
```python
class CalculatorObserver:
    def on_calculation_complete(self, result: float)
    def on_error_occurred(self, error: str)
```

### 4. Strategy Pattern for Number Formatting
```python
class NumberFormatStrategy:
    def format(self, number: float) -> str

class ScientificFormat(NumberFormatStrategy)
class CurrencyFormat(NumberFormatStrategy)
class EngineeringFormat(NumberFormatStrategy)
```

## Quality Assurance Strategy

### Testing Pyramid
1. **Unit Tests** (70%)
   - Individual component testing
   - Mock external dependencies
   - Edge case validation

2. **Integration Tests** (20%)
   - Component interaction testing
   - End-to-end workflow validation
   - Error propagation testing

3. **System Tests** (10%)
   - Full application testing
   - User acceptance testing
   - Performance testing

### Code Quality Metrics
- **Code Coverage**: Target 90%+
- **Cyclomatic Complexity**: < 10 per method
- **Documentation Coverage**: 100% for public APIs
- **Type Hints**: 100% coverage with mypy validation

## Technical Debt Management

### Current Technical Debt
1. **Input validation** scattered across components
2. **Error handling** inconsistent patterns
3. **No configuration management** system
4. **Limited extensibility** for new operations

### Refactoring Priorities
1. **High**: Centralize input validation into dedicated service
2. **Medium**: Implement consistent error handling strategy
3. **Medium**: Add configuration management system
4. **Low**: Extract UI concerns into separate module

## Performance Considerations

### Current Performance Characteristics
- **Memory Usage**: Minimal (stateless operations)
- **CPU Usage**: O(1) for basic operations
- **Startup Time**: < 100ms

### Optimization Opportunities
1. **Caching**: Implement result caching for expensive operations
2. **Lazy Loading**: Load plugins and extensions on demand
3. **Async Operations**: For file I/O and network operations

## Security Considerations

### Current Security Measures
- Input validation prevents code injection
- No external network dependencies
- Safe mathematical operations only

### Future Security Enhancements
- **Input Sanitization**: Enhanced validation for complex expressions
- **Permission System**: Role-based access for advanced features
- **Audit Logging**: Track all calculation operations

## Deployment Strategy

### Current Deployment
- Single Python file execution
- No external dependencies beyond standard library

### Future Deployment Options
1. **Package Distribution**: PyPI package with setup.py
2. **Containerization**: Docker container for consistent environments
3. **Web Application**: Flask/FastAPI web interface
4. **Desktop Application**: Tkinter/PyQt GUI wrapper

## Getting Started

### Prerequisites
- Python 3.7+
- No external dependencies required

### Running the Application
```bash
python main.py
```

### Development Setup
```bash
# Clone repository
git clone <repository-url>
cd calculator

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies (future)
pip install -r requirements-dev.txt

# Run tests (future)
pytest tests/
```

---

*This architecture document follows agile principles and will be updated iteratively as the project evolves.*
