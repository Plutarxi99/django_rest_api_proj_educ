from rest_framework.permissions import BasePermission


class ModeratorOrOwnerCourse(BasePermission):
    """
    Класс для прав модератора, он ни может не создать и удалить курс или урок, но может смотреть и патчить
    """

    def has_permission(self, request, view):
        if view.action in ['create']:
            if request.user.has_one_of_groups('moderator'):
                return False
            return True
        elif view.action in ['destroy']:
            if request.user.has_one_of_groups('moderator') or request.user != view.get_object().owner:
                return False
            return True
        elif view.action in ['retrieve', 'update', 'partial_update']:
            if request.user == view.get_object().owner:
                return True
        return True


class InModeratorLesson(BasePermission):
    """
    Если ты модератор, то не сможешь создавать
    """
    def has_permission(self, request, view):
        if request.user.has_one_of_groups('moderator'):
            return False
        return True


class InModeratorOrOwnerLesson(BasePermission):
    """
    Если пользваотель присоединен к группе moderator, то он может удалять свое, но удалять чужое запрещено,
    также идёт обработка пользователя, если владелец, то разрешено удалять
    """

    def has_permission(self, request, view):
        if request.user.has_one_of_groups('moderator'):
            if view.get_object().course.owner == request.user:
                return True
        elif view.get_object().course.owner == request.user:
            return True
        return False


# class InOwnerLesson(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user
