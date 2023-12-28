from __future__ import annotations

import random

import matplotlib.pyplot as plt
from matplotlib.widgets import Button


class MatrixGenerator:
    @staticmethod
    def generate_random_matrix(rows, cols):
        matrix = [
            [
                random.choices([0, 1, 2], weights=[0.2, 0.75, 0.05])[0]
                for _ in range(cols)
            ]
            for _ in range(rows)
        ]
        return matrix


class CellFinder:
    @staticmethod
    def find_cells(matrix):
        rows, cols = len(matrix), len(matrix[0])
        queue = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 2:
                    queue.append((i, j))

        return queue


class MatrixUpdater:
    @staticmethod
    def update_matrix(matrix, queue):
        rows, cols = len(matrix), len(matrix[0])
        _iter = 0

        while queue:
            _iter += 1
            size = len(queue)
            new_queue = []

            for _ in range(size):
                x, y = queue.pop()

                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if (
                        0 <= nx < rows and 0 <= ny < cols
                        and matrix[nx][ny] == 1
                    ):
                        matrix[nx][ny] = 2
                        new_queue.append((nx, ny))

            queue = new_queue
            yield matrix, _iter

        if any(1 in row for row in matrix):
            return -1, _iter

        return _iter


class MatrixVisualizer:
    @staticmethod
    def visualize_matrix(matrix, matrix_updater):
        fig, ax = plt.subplots()
        im = ax.imshow(matrix, cmap='RdYlGn')
        plt.colorbar(im, ticks=[0, 1, 2], label='Value')

        def next_view(event):
            global _iter
            try:
                updated_matrix, _iter = next(matrix_updater)
                im.set_array(updated_matrix)
                fig.canvas.draw()

            except StopIteration:
                plt.close()
                if any(1 in row for row in matrix):
                    print('Not all yellow cells have been painted.')
                    print(f'Number of {_iter = }')
                else:
                    print('All yellow cells have been painted.')
                    print(f'Number of {_iter = }')

        def on_key(event):
            if event.key == 'right':
                next_view(None)

        fig.canvas.mpl_connect('key_press_event', on_key)

        axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
        bnext = Button(axnext, 'Next iter')
        bnext.on_clicked(next_view)

        plt.show()


def main():
    rows, cols = random.randint(5, 10), random.randint(5, 10)
    matrix = MatrixGenerator.generate_random_matrix(rows, cols)
    queue = CellFinder.find_cells(matrix)
    matrix_updater = MatrixUpdater.update_matrix(matrix, queue)

    MatrixVisualizer.visualize_matrix(matrix, matrix_updater)


if __name__ == '__main__':
    main()
