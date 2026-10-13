---
layout: default
title: Amoxicillin
parent: Solo Predicción del Modelo (L5)
nav_order: 54
evidence_level: L5
indication_count: 8
---

# Amoxicillin
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **8** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Amoxicilina: De Amoxicilina con Inhibidor de Beta-lactamasa a Síndrome de Hiperviscosidad Policlonal

## Resumen en Una Frase

Amoxicilina es un antibiótico betalactámico, registrado en Colombia como "amoxicilina y beta-lactamasa inhibidor".
El modelo TxGNN predice que podría ser efectivo para **síndrome de hiperviscosidad policlonal**,
pero actualmente **no hay ensayos clínicos ni publicaciones** que respalden esta predicción; es solo una predicción del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | Amoxicilina y beta-lactamasa inhibidor |
| Nueva Indicación Predicha | Síndrome de hiperviscosidad policlonal |
| Puntaje de Predicción TxGNN | 99.63% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | Solo registros cancelados |
| Número de Registros Sanitarios | 1 (cancelado) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción registrado para este informe. Según la información conocida, amoxicilina es un antibacteriano betalactámico que inhibe la síntesis de la pared celular bacteriana, y su eficacia en infecciones bacterianas está bien establecida.

El síndrome de hiperviscosidad policlonal es un trastorno hematológico relacionado con las proteínas en sangre, sin un factor bacteriano causal. Por ello, **no se identifica un vínculo mecanístico plausible** entre el fármaco y esta enfermedad.

El puntaje alto (99.63%) refleja únicamente una predicción del modelo, probablemente debida a patrones de la red de conocimiento y no a una base biológica. Otras predicciones con el mismo puntaje (hiperamilasemia, analbuminemia congénita) tampoco tienen sustento mecanístico ni clínico.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada | Estado |
|---------|------|------|-----------|------|
| 20189193 | AMOXIDAL PLUS 600 POLVO PARA RECONSTITUIR A SUSPENSION ORAL | Polvo para reconstituir a suspensión oral | Amoxicilina y beta-lactamasa inhibidor | Cancelado |

---

## Consideraciones de Seguridad

- **Contraindicaciones según el grafo de conocimiento (no provienen del prospecto)**: el grafo de conocimiento asocia amoxicilina con las siguientes condiciones, que deben interpretarse con cautela:
  - Hepáticas y biliares: insuficiencia hepática, enfermedad hepática, colestasis (incluida la colestasis intrahepática recurrente benigna y la familiar), enfermedad de la vesícula biliar.
  - Renales: enfermedad renal, piouréter.
  - Cardíacas: síndrome de QT largo, torsades de pointes, taquicardia ventricular (incluidas las formas catecolaminérgica e infantil incesante).
  - Porfirias: porfiria hereditaria, enfermedad del metabolismo de porfirinas, porfiria.
  - Gastrointestinales: colitis por *Clostridium difficile*, enterocolitis necrotizante perinatal.
  - Neuromusculares: miastenia gravis (incluida la del adulto), enfermedad de la unión neuromuscular.
  - Óseas: osteoporosis, osteoporosis posmenopáusica, fractura ósea.
  - Infecciosas: mononucleosis infecciosa, síndrome de infección crónica por virus de Epstein-Barr.
- **Interacciones Farmacológicas** (100 interacciones registradas; ejemplos principales):
  - **Mayor**: metotrexato; vacuna viva de *Vibrio cholerae* (cepa CVD 103-HgR).
  - **Moderada**: doxiciclina, minociclina, demeclociclina, etinilestradiol, estradiol, anisindiona, dicumarol, balsalazida, entecavir, micofenolato de mofetilo, probióticos (*Lactobacillus acidophilus*, *Bifidobacterium longum infantis*), indio In-111 oxiquinolina.
  - **Menor**: alopurinol, amilorida, azitromicina, claritromicina, eritromicina.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para síndrome de hiperviscosidad policlonal se basa solo en el puntaje del modelo (nivel L5), sin ensayos, sin literatura y sin mecanismo plausible. Además, el único registro sanitario en Colombia está cancelado.

**Para avanzar se necesita:**
- Datos del mecanismo de acción y del prospecto (advertencias y contraindicaciones oficiales), actualmente incompletos.
- Una hipótesis biológica que justifique el uso de un antibiótico en esta enfermedad; de lo contrario, no se recomienda continuar.
- Evaluar candidatas alternativas con mayor plausibilidad. Por ejemplo, la peste septicémica (nivel L4) es biológicamente plausible, pero se apoya solo en estudios in vitro y en animales, y los betalactámicos no son el tratamiento de primera línea.
- Confirmar la situación comercial del fármaco en Colombia, ya que no hay registros vigentes.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

