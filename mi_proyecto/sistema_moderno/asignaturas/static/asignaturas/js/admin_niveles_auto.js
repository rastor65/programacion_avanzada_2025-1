// admin_niveles_auto.js
(function() {
    function getNivelesPorEducativo(valor) {
        if (valor === 'PRIMARIA') {
            return ['1', '2', '3', '4', '5'];
        } else if (valor === 'BACHILLERATO') {
            return ['6', '7', '8', '9', '10', '11'];
        } else if (valor === 'TODOS') {
            return ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'];
        }
        return [];
    }

    document.addEventListener('DOMContentLoaded', function() {
        var selectNivel = document.getElementById('id_nivel_educativo');
        var checkboxes = document.querySelectorAll('.niveles-checkboxes input[type="checkbox"]');
        if (!selectNivel || !checkboxes.length) return;

        selectNivel.addEventListener('change', function() {
            var niveles = getNivelesPorEducativo(this.value);
            checkboxes.forEach(function(checkbox) {
                checkbox.checked = niveles.includes(checkbox.value);
            });
        });
    });
})();
 