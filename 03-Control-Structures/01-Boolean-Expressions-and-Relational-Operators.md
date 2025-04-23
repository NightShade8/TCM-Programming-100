# 🌐 Active Directory (AD) Overview

Active Directory (AD) is a directory service developed by Microsoft for Windows domain networks. It provides a variety of services, including authentication, authorization, and directory management. Here's an overview of its key components and functionality:

## 🗂️ Key Components

- **Domain**: A logical grouping of objects (e.g., users, computers, and devices) that share the same AD database.
- **Domain Controller (DC)**: A server that hosts the AD database and provides authentication and authorization services.
- **Organizational Units (OUs)**: Containers used to organize objects within a domain for easier management.
- **Forest**: A collection of one or more domains that share a common schema and global catalog.
- **Global Catalog (GC)**: A distributed data repository that contains information about every object in the forest.

## 🔑 Authentication and Authorization

AD uses protocols like Kerberos and NTLM for secure authentication and access control:

- **Kerberos**: A secure protocol for authenticating users and devices in a network.
- **NTLM**: A challenge-response authentication protocol for legacy systems.

## 🛠️ Key Features

- **Group Policy**: Enables centralized management of user and computer settings.
- **Replication**: Ensures that changes made on one domain controller are synchronized across all domain controllers in the domain.
- **Trust Relationships**: Allow users in one domain to access resources in another domain.

## 📋 Example Use Cases

1. **User Authentication**: Verifying user credentials when logging into a Windows system.
2. **Resource Access**: Controlling access to shared files, printers, and applications.
3. **Centralized Management**: Applying security policies and configurations across multiple devices.

## 🧩 Integration with Other Services

AD integrates seamlessly with other Microsoft services, such as:

- **Azure Active Directory (Azure AD)**: Extends AD capabilities to the cloud.
- **Microsoft 365**: Provides identity and access management for cloud-based applications.

### 🚀 Why Use Active Directory?

- Simplifies user and resource management.
- Enhances security through centralized authentication.
- Scales to meet the needs of small to large organizations.

Active Directory is a cornerstone of enterprise IT infrastructure, enabling efficient and secure management of users, devices, and resources.