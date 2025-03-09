import numpy as np
import matplotlib.pyplot as plt

# 함수: 2p 오비탈 (p_z 방향)의 확률 밀도 샘플링
def generate_2p_orbital_points(N=100000, a0=1.0, max_r=5.0):
    # 구좌표 난수 생성
    r = np.random.random(N) * max_r * a0
    theta = np.random.random(N) * np.pi
    phi = np.random.random(N) * 2 * np.pi

    # 2p_z 파동함수 및 확률 밀도 계산
    psi_2p_z = (1 / (4 * np.sqrt(2 * np.pi * a0**3))) * (r / a0) * np.exp(-r / (2 * a0)) * np.cos(theta)
    prob_density = np.abs(psi_2p_z) ** 2

    # 확률 밀도 기반 필터링
    sample_prob = np.random.random(N)
    valid_points = sample_prob <= prob_density / np.max(prob_density)

    # 필터링된 점 반환
    return r[valid_points], theta[valid_points], phi[valid_points]

# 함수: 시각화
def plot_orbital(r, theta, phi, title='2p_z Orbital Probability Density'):
    # 구좌표 -> 직교좌표 변환
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    # 3D 시각화
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(x, y, z, s=1, alpha=0.6, c=z, cmap='plasma')  # z축에 따른 컬러맵
    plt.colorbar(scatter, ax=ax, label='height')

    # 그래프 설정
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

    # 축 범위 고정
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.set_zlim([-5, 5])

    plt.show()

# 메인 코드
if __name__ == "__main__":
    # 2p_z 오비탈 샘플링
    r, theta, phi = generate_2p_orbital_points(N=100000, a0=1.0, max_r=5.0)
    # 시각화
    plot_orbital(r, theta, phi)
