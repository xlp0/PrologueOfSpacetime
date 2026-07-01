# Action Plan: Edge Computing Deployment

**Date Created**: April 7, 2026  
**Status**: Active Action Plan  
**Primary Focus**: Hardware Vendor Sourcing, Maintenance Partners, and SDK Research

---

## Overview

Based on technical requirements and deployment constraints, this action plan outlines the comprehensive tasks required to successfully deploy edge AI computing infrastructure for the SHOPPER ANALYTICS system. The plan prioritizes vendor identification, maintenance strategy, and software stack validation.

---

## Critical Tasks

### 1. Hardware Vendor Sourcing (Nvidia & LiDAR)

**Objective**: Identify and establish relationships with reliable local hardware vendors in Jakarta/Indonesia.

#### A. Edge AI Computing Platform Vendors

**Primary Focus**: Nvidia Jetson Orin Nano 8GB
- **Rationale**: Cost-effective solution capable of handling 10-12 cameras simultaneously using DeepStream SDK
- **Performance**: 40 TOPS (INT8), 8GB memory, proven edge AI performance
- **Target Vendors**:
  - Digiware Store (Jakarta area)
  - Seeed Studio Indonesia (Authorized Distributor)
  - Element14 Indonesia (B2B Electronics)
  - RS Components Indonesia
  - Tokopedia/Bukalapak Official Stores

**Action Items**:
- Contact each vendor for product availability and quotations
- Verify stock levels for immediate procurement
- Request bulk pricing for 10+ units
- Confirm warranty terms and local support
- Establish backup vendor relationships
- Compare pricing with international alternatives

#### B. LiDAR Component Sourcing

**Challenge**: LiDAR units require custom assembly from individual components.

**Bill of Materials (per unit)**:
1. 2x X2 360-degree LiDAR Sensor
2. 1x MG996R Servo Motor
3. 1x ESP32 Microcontroller
4. 1x Power Supply 5V 3A
5. Mounting hardware and cables

**Target Vendors**:
- **Tokopedia**: Robot Indonesia, Toko Robot, Elektronik Mart
- **Bukalapak**: Toko Elektronik Jakarta, Komponen Robotik
- **Physical Stores**: Glodok Plaza, Harco Glodok (Jakarta)
- **Specialized Shops**: Toko Robot Indonesia (South Jakarta), Robotic Shop (Central Jakarta)
- **International**: AliExpress/Alibaba (bulk orders, 100+ units)

**Action Items**:
- Survey online marketplaces for component availability
- Visit Glodok for hands-on inspection and price negotiation
- Contact specialized robotics stores for custom assembly quotes
- Research international import feasibility for bulk procurement
- Compare total cost: local assembly vs international import

---

### 2. Maintenance & Support Strategy

**Critical Challenge**: The primary concern is not initial installation, but ongoing maintenance and repair when devices fail on-site.

**Requirements**:
- Local IT partners in Jakarta (not Bali)
- Field technicians available for on-call service
- Project-based contracts (not permanent employees)
- Hardware and software troubleshooting capability
- Emergency repair response capability

#### A. Managed Service Providers (MSP)

**Tier 1 - Critical Issues (24/7 Support)**

**Candidates**:
1. **Lintasarta (PT Lintas Arta)**
   - Enterprise MSP with nationwide coverage
   - 24/7 support with SLA-based contracts
   - Contact: https://www.lintasarta.co.id/

2. **Datacomm Diangraha**
   - IT infrastructure specialist
   - Experience with enterprise hardware
   - Contact: https://www.datacomm.co.id/

3. **Sigma Cipta Caraka (Telkom Group)**
   - Government-backed IT solutions provider
   - Nationwide coverage via Telkom network
   - Contact: https://www.sigma.co.id/

#### B. Local IT Contractors

**Tier 2 - Routine Maintenance**

**Sourcing Channels**:
- Google search: "IT support Jakarta" or "teknisi komputer Jakarta"
- Freelance platforms: Upwork, Sribulancer, Projects.co.id
- University partnerships: UI, ITB, Binus (Computer Science/Engineering departments)

**Engagement Model**:
- On-call basis, no retainer required
- Project-based contracts
- Pool of 3-5 contractors for redundancy
- Coverage: Software updates, minor repairs, routine maintenance

#### C. Training Program Development

**Critical Need**: Prepare comprehensive training materials for local technicians.

**Training Scope**:
- Installation procedures and best practices
- Hardware troubleshooting and diagnostics
- Software configuration and updates
- System monitoring and maintenance
- Emergency repair protocols

**Action Items**:
- Develop detailed training curriculum
- Create hands-on lab environment (1 Jetson + 3 cameras + 1 LiDAR)
- Prepare training materials (slides, videos, SOPs)
- Design practical assessment tests
- Schedule pilot training sessions
- Establish certification levels (Basic, Intermediate, Advanced)

---

### 3. SDK & Software Stack Research

**Objective**: Validate availability, licensing, and suitability of required software development kits.

#### A. NVIDIA Shopper Analytics SDK Research

**Primary Research Focus**:
- Search for NVIDIA-specific Shopper Analytics SDK or libraries
- Verify if SDK is open source and freely downloadable
- Investigate NVIDIA Metropolis Retail Analytics workflow
- Check integration compatibility with existing codebase

**Research Channels**:
- Google search: "NVIDIA Shopper Analytics SDK"
- NVIDIA Developer website and documentation
- GitHub repositories (NVIDIA-AI-IOT, NVIDIA-Metropolis)
- NVIDIA Developer Forums
- AI-assisted research (ChatGPT, Claude, Perplexity)

**Key Questions**:
1. Is there a dedicated Shopper Analytics SDK from NVIDIA?
2. What is the licensing model (open source, commercial, free)?
3. Are there pretrained models for retail environments?
4. How does it integrate with DeepStream SDK?
5. What support is available for production deployment?

#### B. DeepStream SDK Optimization

**Verified Status**: Available, Free, Commercial Use Allowed

**Research Topics**:
- Multi-stream optimization for 10-12 cameras per Jetson Orin Nano
- TensorRT optimization for YOLOv11n inference
- Custom plugin development for homography transformation
- NvDCF tracker configuration for retail tracking
- Metadata pipeline optimization for real-time analytics

**Documentation Resources**:
- DeepStream Developer Guide: https://docs.nvidia.com/metropolis/deepstream/
- GitHub: https://github.com/NVIDIA-AI-IOT/deepstream_python_apps
- TensorRT Optimization: https://docs.nvidia.com/deeplearning/tensorrt/

#### C. NVIDIA Metropolis Early Access

**Status**: Early Access Program (Application Required)

**Action Items**:
- Apply for Metropolis Early Access via NVIDIA website
- Contact NVIDIA Indonesia (apac-sales@nvidia.com, +65 6407 8000)
- Request demo/consultation for retail use case
- Verify pretrained models for Indonesian retail environments
- Check reference architecture for 100+ camera deployment

---

### 4. Documentation & Administration

**Objective**: Consolidate all research findings into formal documentation for decision-making.

#### A. Vendor Research Documentation

**Required Content**:
- Complete vendor contact list with company details
- Product specifications and availability status
- Pricing quotations (bulk and retail)
- Warranty terms and support policies
- Delivery timelines and logistics
- Backup vendor alternatives

**Deliverable**: Comprehensive vendor comparison matrix

#### B. Maintenance Partner Documentation

**Required Content**:
- MSP candidates with service offerings
- Local IT contractor pool details
- SLA requirements and response times
- Contract templates (project-based)
- Training curriculum outline
- Escalation procedures

**Deliverable**: Maintenance strategy document with partner shortlist

#### C. SDK Research Documentation

**Required Content**:
- SDK availability and licensing status
- Integration requirements and compatibility
- Performance benchmarks and optimization strategies
- Community resources and support channels
- Implementation roadmap

**Deliverable**: Technical feasibility report

#### D. Budget Recalculation

**Objective**: Calculate total deployment costs based on local vendor pricing.

**Cost Components**:
- Hardware procurement (Jetson units, cameras, LiDAR components)
- Network infrastructure (switches, cables, accessories)
- Installation labor and setup
- Training development and delivery
- Maintenance contracts (MSP + local contractors)
- Operational expenses (electricity, internet, spare parts)

**Analysis Required**:
- Compare edge computing costs vs cloud operational expenses
- Calculate break-even timeline
- Assess long-term ROI and cost savings
- Identify budget optimization opportunities

**Deliverable**: Budget breakdown with cloud comparison analysis

## Key Contacts & Resources

### Hardware Vendors

**Digiware Store** (Primary)
- Website: https://digiwarestore.com/
- Product: NVIDIA Jetson AGX Orin 64GB Developer Kit
- Contact: https://digiwarestore.com/en/contact-us

**Alternative Vendors**:
- Seeed Studio Indonesia: https://www.seeedstudio.com/
- Element14 Indonesia: sales.id@element14.com
- RS Components Indonesia: https://id.rs-online.com/

### Maintenance Partners

**Managed Service Providers**:
- Lintasarta: https://www.lintasarta.co.id/
- Datacomm Diangraha: https://www.datacomm.co.id/
- Sigma Cipta Caraka: https://www.sigma.co.id/

**University Partnerships**:
- Universitas Indonesia (UI) - Computer Science Department
- Institut Teknologi Bandung (ITB) - Engineering Department
- Binus University - Computer Science Department

### NVIDIA Resources

**NVIDIA Indonesia**:
- Email: apac-sales@nvidia.com
- Phone: +65 6407 8000 (Singapore office, covers Indonesia)
- Website: https://www.nvidia.com/en-sg/

**SDK Documentation**:
- DeepStream SDK: https://docs.nvidia.com/metropolis/deepstream/
- TensorRT: https://docs.nvidia.com/deeplearning/tensorrt/
- GitHub: https://github.com/NVIDIA-AI-IOT/deepstream_python_apps

---

**Document Status**: Active Action Plan  
**Created**: April 7, 2026  
**Owner**: SHOPPER ANALYTICS Team  
**Next Review**: After Week 1 vendor research completion
