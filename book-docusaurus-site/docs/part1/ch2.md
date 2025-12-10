---
id: ch2
title: Robotics Fundamentals
slug: /part1/ch2
---

# Robotics Fundamentals

## 2.1 Introduction to Robotics

Robotics is an interdisciplinary field that integrates computer science and engineering to design, construct, operate, and use robots. The goal of robotics is to create machines that can assist humans in various tasks, ranging from industrial automation to exploration and personal assistance. This chapter provides a foundational understanding of the core principles that govern robot design and operation.

## 2.2 Robot Kinematics

Kinematics deals with the study of motion without considering the forces that cause it. In robotics, kinematics is crucial for understanding how a robot's joints and links move in space.

### 2.2.1 Degrees of Freedom (DoF)

The **Degrees of Freedom (DoF)** of a robot defines the number of independent parameters required to uniquely specify its configuration in space. For a rigid body in 3D space, it has 6 DoF (3 for position: x, y, z; and 3 for orientation: roll, pitch, yaw). Robotic manipulators typically have multiple joints, each contributing one or more DoF.

### 2.2.2 Forward Kinematics

**Forward Kinematics** is the process of calculating the position and orientation of the robot's end-effector (e.g., a gripper or tool) given the values of its joint variables (angles for revolute joints, displacements for prismatic joints). This is typically solved using transformation matrices (e.g., Denavit-Hartenberg parameters) that describe the relative position and orientation of each link's coordinate frame with respect to its predecessor.

**Example: 2-DOF Planar Arm**
Consider a 2-DOF planar robot arm with two revolute joints and link lengths $L_1$ and $L_2$. If the joint angles are $\theta_1$ and $\theta_2$, the end-effector position $(x, y)$ can be calculated as:
$x = L_1 \cos(\theta_1) + L_2 \cos(\theta_1 + \theta_2)$
$y = L_1 \sin(\theta_1) + L_2 \sin(\theta_1 + \theta_2)$

### 2.2.3 Inverse Kinematics

**Inverse Kinematics** is the more challenging problem of determining the joint variables required to achieve a desired position and orientation of the end-effector. This often involves non-linear equations and can have multiple solutions, no solutions, or singularities. Solutions typically involve analytical methods (for simpler configurations) or numerical iterative methods (for complex robots).

## 2.3 Robot Dynamics

Dynamics extends kinematics by considering the forces and torques that cause motion. It is essential for understanding robot control, motor sizing, and interaction forces.

### 2.3.1 Newton-Euler and Lagrangian Formulations

Robot dynamics can be formulated using either the **Newton-Euler** approach (which considers forces and moments on individual links) or the **Lagrangian** approach (which uses energy conservation principles). Both methods yield equations of motion that relate joint torques to joint accelerations, velocities, and positions, as well as external forces.

### 2.3.2 Mass, Inertia, and Friction

Key physical properties influencing dynamics include the mass and inertia of each link, and frictional forces within the joints. Accurate dynamic models are critical for precise force control, compliant motion, and understanding a robot's interaction with its environment.

## 2.4 Robot Manipulators and Mobile Robots

Robots can be broadly categorized based on their primary function and mobility.

### 2.4.1 Robot Manipulators (Industrial Arms)

**Robot manipulators** are typically fixed-base robots designed for precise manipulation tasks. They consist of a series of links connected by joints, allowing them to reach and manipulate objects within a defined workspace. Common types include:
*   **Cartesian (Gantry)**: Rectangular workspace, uses prismatic joints (e.g., pick-and-place).
*   **Cylindrical**: Cylindrical workspace, uses one revolute and two prismatic joints.
*   **Spherical (Polar)**: Spherical workspace, uses two revolute and one prismatic joint.
*   **Articulated (SCARA, Revolute)**: Human-like arms with multiple revolute joints, versatile for assembly.

### 2.4.2 Mobile Robots

**Mobile robots** are capable of movement within an environment. Their locomotion systems vary widely depending on the application:
*   **Wheeled Robots**: Common in industrial settings, easy to control (e.g., AGVs, AMRs).
*   **Legged Robots**: Offer high maneuverability over uneven terrain, more complex to control (e.g., bipedal humanoids, quadruped robots).
*   **Aerial Robots (Drones)**: For inspection, surveillance, delivery.
*   **Underwater Robots (ROVs, AUVs)**: For exploration, maintenance.

## 2.5 Sensors and Actuators in Robotics

Sensors and actuators are the interface between the robot's control system and the physical world.

### 2.5.1 Sensors

**Sensors** provide data about the robot's state and environment. They are categorized into:
*   **Proprioceptive Sensors**: Measure internal state (e.g., joint encoders for position, accelerometers for orientation/acceleration, force/torque sensors at wrists).
*   **Exteroceptive Sensors**: Measure external environment (e.g., cameras for vision, LiDAR/ultrasonic for range, microphones for audio, touch sensors).

### 2.5.2 Actuators

**Actuators** convert control signals into physical motion.
*   **Electric Motors**: The most common type (DC servo motors, stepper motors, brushless DC motors) for precise position and velocity control.
*   **Hydraulic/Pneumatic Actuators**: Provide high force and power density, often used in heavy industrial robots.
*   **Compliant Actuators**: Designed for safe human-robot interaction, allowing for controlled deformation.

## 2.6 Robot Control Strategies

Robot control aims to ensure the robot performs desired actions accurately and stably.

### 2.6.1 Open-Loop Control

In **open-loop control**, the control action is independent of the system's output. The controller sends commands without receiving feedback on whether the desired state was achieved. This is simpler but highly sensitive to disturbances and model inaccuracies.
**Example**: A conveyor belt running at a constant speed regardless of load.

### 2.6.2 Closed-Loop Control (Feedback Control)

**Closed-loop control**, also known as feedback control, uses sensor feedback to continuously adjust the control action. The difference between the desired state (setpoint) and the actual state (measured by sensors) generates an error signal, which the controller uses to modify its output. This makes the system robust to disturbances and uncertainties.

### 2.6.3 PID Control

The **Proportional-Integral-Derivative (PID) controller** is one of the most widely used feedback control algorithms. It calculates an error value as the difference between a measured process variable and a desired setpoint. The controller attempts to minimize the error by adjusting the process control inputs.
*   **Proportional (P)**: Output is proportional to the current error.
*   **Integral (I)**: Output is proportional to the accumulation of past errors, helping eliminate steady-state errors.
*   **Derivative (D)**: Output is proportional to the rate of change of the error, providing damping and reducing overshoot.

## Summary

Robotics fundamentals are built upon kinematics (motion without forces), dynamics (motion with forces), and the physical components of robots (manipulators, mobile platforms, sensors, and actuators). Kinematics allows for calculating end-effector positions (forward kinematics) and joint configurations for desired positions (inverse kinematics). Dynamics considers the forces influencing motion, crucial for control. Robots employ various sensor types for perception and actuators for action. Control strategies, particularly closed-loop feedback systems like PID controllers, are essential for achieving precise, stable, and adaptive robot behaviors in complex environments.

## Exercises

1.  **Kinematics Calculation**: For a 3-DOF robotic arm with revolute joints, explain the concept of forward kinematics. Provide a conceptual outline of how Denavit-Hartenberg parameters would be used to solve it.
2.  **Dynamics vs. Kinematics**: Differentiate between robot kinematics and dynamics. Why is understanding dynamics critical for tasks involving physical interaction, such as pushing an object or human-robot collaboration?
3.  **Robot Types**: Describe two distinct types of robot manipulators and two distinct types of mobile robots. For each, provide a typical application and discuss one advantage and one disadvantage of its design for that application.
4.  **Sensors & Actuators**: Choose a specific robotic application (e.g., autonomous driving car, surgical robot). Identify three essential sensors and three essential actuators for this robot, explaining their function and why they are critical.
5.  **Control Systems**: Explain the difference between open-loop and closed-loop control in robotics. Provide a simple example where closed-loop control is absolutely necessary, justifying your answer. How do the P, I, and D terms of a PID controller contribute to overall system performance?