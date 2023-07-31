from manim import *

class BubbleSort(Scene):
    def construct(self):
        # Создаем список из чисел
        num_list = [3, 1, 5, 4, 2, 9, 8, 7, 6]

        # Создаем круги с цифрами внутри
        circles = []
        num_labels = []
        num_elements = len(num_list)
        for i, num in enumerate(num_list):
            # Вычисляем координаты центра для каждого круга
            if num_elements % 2 == 0:
                center_x = (i - num_elements/2 + 0.5) * 1.5
            else:
                center_x = (i - (num_elements-1)/2) * 1.5
            circle = Circle(radius=0.7, color=BLUE).move_to((center_x, 0, 0))
            num_label = Text(str(num), font_size=24).move_to(circle.get_center())
            circles.append(circle)
            num_labels.append(num_label)
        circle_group = VGroup(*circles, *num_labels)
        self.play(Create(circle_group))

        # Сортируем список
        for i in range(len(num_list)):
            sorted = True
            for j in range(len(num_list) - i - 1):
                # Выделяем круги, которые сравниваются
                circles[j].set_color(YELLOW)
                circles[j+1].set_color(YELLOW)
                self.wait(0.5)

                if num_list[j] > num_list[j + 1]:
                    # Анимируем перемещение кругов и цифр
                    move_distance = circles[j].get_center() - circles[j+1].get_center()
                    self.play(
                        circles[j].animate.shift(-move_distance),
                        circles[j+1].animate.shift(move_distance),
                        num_labels[j].animate.move_to(circles[j+1].get_center()),
                        num_labels[j+1].animate.move_to(circles[j].get_center()),
                        rate_func=smooth,
                        run_time=1
                    )
                    # Обновляем список и соответствующие круги и цифры
                    num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                    circles[j], circles[j+1] = circles[j+1], circles[j]
                    num_labels[j], num_labels[j+1] = num_labels[j+1], num_labels[j]
                    sorted = False
                # Сбрасываем выделение цветом кругов
                circles[j].set_color(BLUE)
                circles[j+1].set_color(BLUE)

            if sorted:
                break

        # Визуализируем отсортированные круги с цифрами внутри
        self.play(
            circle_group.animate.scale(0.4).to_edge(UP),
            rate_func=smooth,
            run_time=1
        )
        self.wait()