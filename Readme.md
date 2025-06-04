# Microsoft Fabric Data Pipeline Project

## Overview

This project implements a comprehensive data pipeline solution using Microsoft Fabric, featuring a multi-layered lakehouse architecture for data processing and transformation. The solution includes automated backfill capabilities and follows modern data engineering best practices with proper data governance and testing frameworks.

## Architecture

### Lakehouse Structure

The project implements a medallion architecture with the following data layers:

- **🏠 `lh_landed`** - Raw data ingestion layer
- **📊 `lh_sourced`** - Initial data processing and standardization
- **🧹 `lh_cleansed`** - Data quality and cleansing operations
- **✅ `lh_conformed`** - Business-ready, conformed data models
- **🔒 `lh_conformed_pii`** - PII-compliant conformed data with privacy controls

### Data Flow

```
Raw Data → Landed → Sourced → Cleansed → Conformed → Conformed PII
```

Each layer serves a specific purpose in the data transformation pipeline, ensuring data quality, governance, and compliance requirements are met.

## Components

### Notebooks

- **`nb_backfill.Notebook`** - Main backfill orchestration notebook
  - Handles historical data processing
  - Supports parameterized execution
  - Implements parallel processing with configurable concurrency
  - Manages dependencies between pipeline stages

### Environment Configuration

- **`env_nutter_testing.Environment`** - Testing environment setup
  - Spark compute configuration optimized for testing workloads
  - Dynamic executor allocation (1-9 executors)
  - Memory-optimized settings (56GB driver, 56GB executor memory)
  - Native execution engine disabled for compatibility

## Key Features

### 🔄 Backfill Processing
- **Date Range Processing**: Configurable date intervals for historical data processing
- **Parallel Execution**: Concurrent processing of multiple date ranges
- **Dependency Management**: Automatic dependency resolution between pipeline stages
- **Parameter Support**: Runtime parameter injection for flexible execution

### 🏗️ Pipeline Orchestration
- **DAG Generation**: Automatic pipeline DAG creation with proper dependencies
- **Activity Management**: Structured activity execution with timeout controls
- **Error Handling**: Built-in error handling and retry mechanisms
- **Monitoring**: Pipeline execution monitoring and logging

### ⚙️ Configuration Management
- **Environment-specific Settings**: Separate configurations for different environments
- **Spark Optimization**: Tuned Spark configurations for optimal performance
- **Resource Management**: Dynamic resource allocation based on workload

## Getting Started

### Prerequisites

- Microsoft Fabric workspace access
- Appropriate permissions for lakehouse operations
- Spark compute environment configured

### Configuration

1. **Environment Setup**
   ```yaml
   # Spark Configuration (env_nutter_testing.Environment/Setting/Sparkcompute.yml)
   driver_cores: 8
   driver_memory: 56g
   executor_cores: 8
   executor_memory: 56g
   dynamic_executor_allocation:
     enabled: true
     min_executors: 1
     max_executors: 9
   ```

2. **Pipeline Parameters**
   ```python
   # Backfill Parameters
   trigger_time = '2024-08-09T00:00:00Z'
   from_date = '2022-08-01T00:00:00Z'
   to_date = '2024-08-09T23:59:59Z'
   source_system = 'example_system'
   table_name = 'example_table'
   ```

### Running the Pipeline

1. **Manual Execution**
   - Open the `nb_backfill.Notebook`
   - Configure parameters in the parameter cell
   - Execute all cells sequentially

2. **Automated Execution**
   - Use Data Factory pipelines for scheduled execution
   - Parameters can be overridden at runtime
   - Supports integration with orchestration tools

## Pipeline Workflow

### Step 1: Import Dependencies
- Load common libraries and helper functions
- Initialize global configurations

### Step 2: Parameter Configuration
- Define execution parameters (dates, source system, table name)
- Support for runtime parameter override

### Step 3: Configuration Extraction
- Load DAG-specific configurations
- Set timeout and concurrency parameters

### Step 4: DAG Generation
- Generate date intervals for processing
- Create sourced layer activities with dependencies
- Build cleansed layer activities
- Construct complete pipeline DAG

### Step 5: Pipeline Execution
- Execute the generated DAG using `mssparkutils.notebook.runMultiple()`
- Monitor execution progress and handle errors

## Data Governance

### Security & Compliance
- **PII Handling**: Dedicated lakehouse for PII-compliant data processing
- **Access Control**: Lakehouse-level security and access management
- **Data Lineage**: Trackable data flow through all pipeline stages

### Quality Assurance
- **Testing Environment**: Dedicated Nutter testing environment
- **Data Validation**: Built-in data quality checks at each layer
- **Error Handling**: Comprehensive error handling and logging

## Performance Optimization

### Spark Configuration
- **Memory Optimization**: 56GB driver and executor memory allocation
- **Dynamic Scaling**: Auto-scaling from 1 to 9 executors based on workload
- **Legacy Compatibility**: Time parser policy set to LEGACY for compatibility
- **Message Size**: Increased RPC message size limit for large data transfers

### Pipeline Efficiency
- **Parallel Processing**: Concurrent execution of independent activities
- **Dependency Optimization**: Minimal dependency chains for faster execution
- **Resource Management**: Efficient resource utilization with dynamic allocation

## Monitoring & Troubleshooting

### Logging
- Pipeline execution logs available through Fabric monitoring
- Activity-level logging for detailed troubleshooting
- Error tracking and notification capabilities

### Performance Metrics
- Execution time tracking per activity
- Resource utilization monitoring
- Data volume processing metrics

## Contributing

When contributing to this project:

1. Follow the established naming conventions for lakehouses and notebooks
2. Ensure proper parameter documentation in notebook cells
3. Test changes in the dedicated testing environment
4. Update configuration files as needed for new features

## Support

For issues and questions:
- Check Fabric workspace logs for execution errors
- Review Spark configuration for performance issues
- Validate lakehouse permissions for access problems

---

*This project leverages Microsoft Fabric's native capabilities for scalable data processing and analytics workloads.*
