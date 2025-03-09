import numpy as np
import matplotlib.pyplot as plt

# 함수: 3d 오비탈의 확률 밀도 샘플링
def generate_3d_orbital_points(N=100000, a0=1.0, max_r=10.0, orbital_type="z2"):
    # 구좌표 난수 생성
    r = np.random.random(N) * max_r * a0
    theta = np.random.random(N) * np.pi
    phi = np.random.random(N) * 2 * np.pi

    # 방사 함수 R_{3d}(r)
    radial_part = (1 / np.sqrt(81 * np.pi * a0**5)) * (r / a0)**2 * np.exp(-r / (3 * a0))

    # 각도에 따른 부분
    if orbital_type == "z2":  # d_{z^2}
        angular_part = 3 * np.cos(theta)**2 - 1
    elif orbital_type == "xy":  # d_{xy}
        angular_part = np.sin(theta)**2 * np.sin(2 * phi)
    elif orbital_type == "xz":  # d_{xz}
        angular_part = np.sin(theta) * np.cos(theta) * np.cos(phi)
    elif orbital_type == "yz":  # d_{yz}
        angular_part = np.sin(theta) * np.cos(theta) * np.sin(phi)
    elif orbital_type == "x2-y2":  # d_{x^2-y^2}
        angular_part = np.sin(theta)**2 * np.cos(2 * phi)
    else:
        raise ValueError("Invalid orbital type! Choose from 'z2', 'xy', 'xz', 'yz', 'x2-y2'.")

    # 전체 파동함수 및 확률 밀도
    psi_3d = radial_part * angular_part
    prob_density = np.abs(psi_3d)**2

    # 확률 밀도 기반 필터링
    sample_prob = np.random.random(N)
    valid_points = sample_prob <= prob_density / np.max(prob_density)

    # 필터링된 점 반환
    return r[valid_points], theta[valid_points], phi[valid_points]

# 함수: 시각화
def plot_orbital(r, theta, phi, title='3d Orbital Probability Density'):
    # 구좌표 -> 직교좌표 변환
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    # 3D 시각화
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(x, y, z, s=1, alpha=0.6, c=z, cmap='coolwarm')  # z축에 따른 컬러맵
    plt.colorbar(scatter, ax=ax, label='height')

    # 그래프 설정
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

    # 축 범위 고정
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

    plt.show()

# 메인 코드
if __name__ == "__main__":
    # 'z2', 'xy', 'xz', 'yz', 'x2-y2' 중에서 선택 가능
    orbital_types = ["z2", "xy", "xz", "yz", "x2-y2"]
    for orbital in orbital_types:
        r, theta, phi = generate_3d_orbital_points(N=100000, a0=1.0, max_r=10.0, orbital_type=orbital)
        plot_orbital(r, theta, phi, title=f"3d_{orbital} Orbital Probability Density")
